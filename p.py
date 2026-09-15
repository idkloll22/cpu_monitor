import os, time


# calculate the percentage of load(load * cores / 100)
def cal_percentage(load_value, cores):
    if cores == 0:
        return 0.0
    return round((load_value / cores) * 100, 2)


# rate how much cpu loads
def performance(percentage):
    threshold = [
        (25, "Sleeping"),
        (50, "Normal"),
        (75, "Heavy"),
        (100, "Overclock"),
    ]

    for limit, label in threshold:
        if percentage < limit:
        return label
    
    return label


def load_monitor(cores):
    # Open proccesing config
    with open("/proc/loadavg", "r") as file:
        content = file.read()


    ps_split = content.split()
    min1_load, min5_load, min15_load = [float(x) for x in ps_split[:3]]

    # unpacking the load
    perc_1, perc_5, perc_15 = [
        cal_percentage(load, cores)
        for load in [min1_load, min5_load, min15_load]
    ]

    # loops and rate the performance
    perf_1, perf_5, perf_15 = [
         performance(percentage)
         for percentage in [perc_1, perc_5, perc_15]
    ]


    print(f"first minutes loads, {min1_load}, {perc_1:.2f}, {perf_1}")
    print(f"five minutes loads, {min5_load},  {perc_5:.2f}, {perf_5}")
    print(f"fiften minustes loads, {min15_load}, {perc_15:.2f}, {perf_15}")


# count many of cpu cores
cpu_cores = os.cpu_count()

# get PID and store in variable
ps_id = os.getpid()


while True:
    try:
       load_monitor(cpu_cores)
       time.sleep(3)
    except KeyboardInterrupt:
        print("--End---")
        break
