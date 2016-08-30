import os
import time
import subprocess


tests = ["shearingsheet", "outersolarsystem_ias15","outersolarsystem_whfast"]
datafile = "rebound_2.20.4.txt"

for test in tests:
    print("Working on %s" %test)
    os.chdir(test)
    os.system("make clean")
    os.system("make")
    start = time.time()
    os.system("./rebound")
    end = time.time()
    os.chdir("../")
    print("time: %f"%(end-start))

    with open(datafile, "a") as f:
        f.write(test+"\t")
        f.write((time.strftime("%Y/%m/%d"))+"\t")
        f.write((time.strftime("%H:%M:%S"))+"\t")
        proc = subprocess.Popen(["hostname"], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        f.write(out.decode().strip()+"\t")
        proc = subprocess.Popen(["uname"], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        f.write(out.decode().strip()+"\t")
        if "Darwin" in out.decode():
            proc = subprocess.Popen(["sysctl -n machdep.cpu.brand_string"], stdout=subprocess.PIPE, shell=True)
        else:
            proc = subprocess.Popen(["grep \"^model name\" -m 1 /proc/cpuinfo"], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        f.write(out.decode().strip()+"\t")
        f.write("%.8f\t"%(end-start))

        f.write("\n")
