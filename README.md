# CPU Load Performace Monitor

A clean way to to see cpu load performance and as well easy to config for bigginers
it can be used for debugging and gaming

# Features
- **Real time Monitor:** Is directly access the linux `~/proc/loadavg` with 3 second refresh
- **auto calculated threshold:** Functional real time calculate percentage of CPU load
- **performance rate:** perfomace rate function is to rate how much percentage of cpu load whatever is normal or overheated
- **Easy to read and can rebuild:** It has only 60+ lines of code with basic syntax bigginer to intermieted
- **Error protection**  The key board interruption no longer gives error instead it will say "end"

# How to install globally
make to work in global or any terminal:

```bash
chmod +x cpu_monitor.py
alias cpu-monitor="\$(pwd)/cpu_monitor.py"
```

# how to run
Simply type your custom command:
```bash
cpu-monitor
```
