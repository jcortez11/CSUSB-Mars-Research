#### SCRIPT WITH DEFINED BOXES
### This is a template to create a dataset of nulls, clouds, ice
### after boxes for each across a few files have been found

## Example of defined known null boxes
boxes_nulls = {'file1': [20, 40, 100, 200], "file2": [50, 100, ]}

# And clouds and ice boxes....
boxes_clouds = ...
boxes_ice = ...

# And functions to grab those boxes from the original files
def load_all_nulls():
    for file in allfiles:
        open_file(file)
        data = grab_nulls(box[file])
        data["target"] = 0 ## Add label for nulls

def load_all_clouds():
    "similar to nulls"
        data["target"] = 1  # Different label for clouds

# Then concatenate nulls, clouds, ice....
def combine(null_data, cloud_data, ice_data):
    return

## Then save output file, this data will be loaded in `train.py`
def save(data):
    data.to_csv("training_test_data.csv", index=False)