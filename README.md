# Error-Detection
Error detection project

# Data Format
Data should be exported to CSV files in the following format:

## Source
Should be exported directly from *Tobii Pro Lab* and should have the following columns in the listed order:
Recording,Participant,Timeline,TOI,Interval,Media,AOI_tag,Event_type,Validity,EventIndex,Start,Stop,Duration,AOI,Hit_proportion,FixationPointX,FixationPointY,Average_pupil_diameter,Saccade_direction,Average_velocity,Peak_velocity,Saccade_amplitude,Start_AOI,Landing_AOI,Start_position_X,Start_position_Y,Landing_position_X,Landing_position_Y,Glance_AOI,Glance_previous_AOI,Glance_next_AOI

Convert the `.tsv` file exported by Tobii Pro Lab to a `.csv` file using the provided script (`scripts/tsv2csv.sh`).
Run it with the following syntax:
```sh
./tsv2csv.sh /path/to/tsv/file/to/convert
```

It will automatically create a `.csv` file in the same directory with the same name.

## Target
Should have the following columns in the listed order:
"Error #","Time start","Time end",Description,Fix
