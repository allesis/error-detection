{
  description = "A Nix-flake-based Python development environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
  };

  outputs = {
    self,
    nixpkgs,
  }: let
    supportedSystems = ["x86_64-linux" "x86_64-darwin"];
    forEachSupportedSystem = f:
      nixpkgs.lib.genAttrs supportedSystems (
        system: let
          pkgs = import nixpkgs {
            inherit system;
          };
          tsv2csv =
            pkgs.writeShellApplication
            {
              name = "tsv2csv";
              runtimeInputs = [
                pkgs.gawk
                pkgs.gnused
                pkgs.coreutils
                pkgs.findutils
              ];
              text = ''
                # Thanks: https://www.datafix.com.au/BASHing/2021-10-13.html
                set -eu
                awk -v FS="\t" -v OFS="," '{for (i=1;i<=NF;i++) {x=gensub(/"/,"\"\"","g",$i); if (x ~ /"/ || x ~ /,/) $i="\""x"\""; else $i=$i}} 1' "$1" | sed "s/\r$//" > "$(echo "$1" | xargs -n 1 basename | sed "s/\..*//")".csv;
              '';
            };
          xlsx2csv =
            pkgs.writeShellApplication
            {
              name = "xlsx2csv";
              runtimeInputs = [
                pkgs.gawk
                pkgs.gnused
                pkgs.coreutils
                pkgs.findutils
                pkgs.xlsx2csv
              ];
              text = ''
                set -eu
                xlsx2csv "$1" "$(echo "$1" | xargs -n 1 basename | sed "s/\..*//")".csv
              '';
            };
          convert_all_tsv2csv =
            pkgs.writeShellApplication
            {
              name = "all_tsv2csv";
              runtimeInputs = [
                tsv2csv
                pkgs.gawk
                pkgs.gnused
                pkgs.coreutils
                pkgs.findutils
              ];
              text = ''
                for file in *.tsv; do
                	tsv2csv "$file"
                done
              '';
            };
          convert_all_xlsx2csv =
            pkgs.writeShellApplication
            {
              name = "all_xlsx2csv";
              runtimeInputs = [
                xlsx2csv
                pkgs.gawk
                pkgs.gnused
                pkgs.coreutils
                pkgs.findutils
              ];
              text = ''
                for file in *.xlsx; do
                	xlsx2csv "$file"
                done
              '';
            };
          get-unique-column-values-from-csv = pkgs.writeShellApplication {
            name = "get-unique-column-values-from-csv";
            runtimeInputs = [];
            text = ''
              # Thanks: https://gist.github.com/thomas-optimove/2616bd242be059fb2ec7cd1762946b15
              # Check for the correct number of arguments
              if [[ $# -ne 2 ]]; then
               echo "Usage: $0 <csv_file> <column_number>"
               exit 1
              fi

              # Arguments
              CSV_FILE="$1"
              COLUMN_NUMBER="$2"

              # Check if the file exists
              if [[ ! -f "$CSV_FILE" ]]; then
               echo "Error: File '$CSV_FILE' not found!"
               exit 1
              fi

              # Check if the column number is valid (greater than 0)
              if [[ ! "$COLUMN_NUMBER" =~ ^[0-9]+$ ]] || [[ "$COLUMN_NUMBER" -lt 1 ]]; then
               echo "Error: Column number must be a positive integer."
               exit 1
              fi

              # Extract the specified column, remove the header, and get unique values
              awk -F, -v column_number="$COLUMN_NUMBER" '
              NR == 1 {
               # Ensure the column number is valid by checking the number of fields
               if (column_number > NF) {
                   print "Error: Column number " column_number " is out of range."
                   exit 1
               }
               next
              }
              {
               print $column_number
              }' "$CSV_FILE" | sort | uniq
            '';
          };
        in
          f {
            pkgs = pkgs;
            tsv2csv = tsv2csv;
            convert_all_tsv2csv = convert_all_tsv2csv;
            xlsx2csv = xlsx2csv;
            convert_all_xlsx2csv = convert_all_xlsx2csv;
            get-unique-column-values-from-csv = get-unique-column-values-from-csv;
          }
      );
  in {
    devShells = forEachSupportedSystem ({
      pkgs,
      tsv2csv,
      get-unique-column-values-from-csv,
      xlsx2csv,
      convert_all_tsv2csv,
      convert_all_xlsx2csv,
    }: {
      default = pkgs.mkShell {
        packages = with pkgs; [
          uv
          python313Packages.jedi-language-server
          black
          just
          just-lsp
          tsv2csv
          get-unique-column-values-from-csv
          xlsx2csv
          convert_all_tsv2csv
          convert_all_xlsx2csv
        ];
      };
    });
  };
}
