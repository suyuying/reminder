import yaml

def read_yaml_data(yaml_file) -> dict:
    with open(yaml_file,'r') as f:
        yaml_data=yaml.safe_load(f)
    return yaml_data

def compare_data(yaml_file,yaml_file_need_to_add):
    yaml_data=read_yaml_data(yaml_file)
    yaml_data_need_to_add=read_yaml_data(yaml_file_need_to_add)
    # ans1

    # for log_data_need_to_add in yaml_data_need_to_add['log_paths']:
    #     is_same_data = False
    #     for log_data in yaml_data['log_paths']:
    #         if log_data_need_to_add['log_path'] == log_data['log_path']:
    #             print(f"same route")
    #             is_same_data=True
    #             break
    #     if is_same_data:
    #         print(f"same route,ignore")
    #     else:
    #         yaml_data['log_paths'].append(log_data_need_to_add)
    # print(yaml_data)
    # with open(f"answer_{yaml_file}",'w') as f:
    #     yaml.safe_dump(yaml_data,f)

    # ans2
    for log_data_need_to_add in yaml_data_need_to_add['log_paths']:
        if any(log_data_need_to_add['log_path'] ==  log_data['log_path'] for log_data in yaml_data['log_paths']):
            print(f"same route,ignore")
        else:
            yaml_data['log_paths'].append(log_data_need_to_add)
    print(yaml_data)
    with open(f"answer_{yaml_file}",'w') as f:
        yaml.safe_dump(yaml_data,f)

if __name__ == "__main__":
    compare_data("data1.yml","data1_need_to_add.yml")
    compare_data("data2.yml", "data2_need_to_add.yml")