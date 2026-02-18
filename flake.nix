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
              runtimeInputs = [pkgs.gawk];
              text = ''
                # Thanks: https://www.datafix.com.au/BASHing/2021-10-13.html
                set -eu
                awk -v FS="\t" -v OFS="," '{for (i=1;i<=NF;i++) {x=gensub(/"/,"\"\"","g",$i); if (x ~ /"/ || x ~ /,/) $i="\""x"\""; else $i=$i}} 1' "$1" | sed "s/\r$//" > "$(echo "$1" | xargs -n 1 basename | sed "s/\..*//")".csv;
              '';
            };
        in
          f {
            pkgs = pkgs;
            tsv2csv = tsv2csv;
          }
      );
  in {
    devShells = forEachSupportedSystem ({
      pkgs,
      tsv2csv,
    }: {
      default = pkgs.mkShell {
        packages = with pkgs; [
          uv
          python313Packages.jedi-language-server
          black
          just
          just-lsp
          tsv2csv
        ];
      };
    });
  };
}
