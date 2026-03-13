import psutil
import sys
import os
import time
import schedule

def CreateLog(FolderName) :
    Border = "-"*60
    Ret = False

    Ret = os.path.exists(FolderName)
    if (Ret == True) :
        Ret = os.path.isdir(FolderName)
        if(Ret == False) :
            print("Unable to create folder")
            return
    else :
        os.mkdir(FolderName)
        print("Directory for log files gets created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName,"Marvellous_%s.log"%timestamp)
    print("File gets created with name : ",FileName)

    fobj = open(FileName,"w")

    fobj.write(Border+"\n")
    fobj.write("----------Marvellous Platform Surveillance System-----------\n")
    fobj.write("Log created at : "+time.ctime()+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("----------------------System Report-------------------------\n")
    #print("CPU Usage : ",psutil.cpu_percent())
    fobj.write("CPU Usage : %s %%\n" %psutil.cpu_percent())

    fobj.write(Border+"\n")
    
    mem = psutil.virtual_memory()
    #print("RAM Usage : ",mem.percent)
    fobj.write("RAM Usage : %s %%\n" %mem.percent)

    fobj.write(Border+"\n")

    fobj.write("Disk Usage Report \n")
    for part in psutil.disk_partitions() :
        try : 
            usage = psutil.disk_usage(part.mountpoint)
            #print(f"{part.mountpoint} used {usage.percent}%%")
            fobj.write("%s -> %s %% used\n" %(part.mountpoint, usage.percent))
        except :
            pass

    fobj.write(Border+"\n")

    net = psutil.net_io_counters()            # used to get data sent and received from internet
    fobj.write("Network Usage Report\n")
    fobj.write("Sent : %.2f MB\n" %(net.bytes_sent / (1024*1024)))  
    fobj.write("Receive : %.2f MB\n" %(net.bytes_recv / (1024*1024)))

    # Process LOG
    Data = ProcessScan()

    
    for info in Data :
        fobj.write("PID : %s\n" %info.get("pid"))
        fobj.write("Name : %s\n" %info.get("name"))
        fobj.write("UserName : %s\n" %info.get("username"))
        fobj.write("Status : %s\n" %info.get("status"))
        fobj.write("Start Time : %s\n" %info.get("create_time"))
        fobj.write("CPU %% : %.2f\n" %info.get("cpu_percent"))
        fobj.write("Memory %% : %.2f\n" %info.get("memory_percent"))
        fobj.write("Thread Count : %.2f\n" %info.get("num_threads"))
        fobj.write("Number of Files Opened : %s\n" %info.get("open_files"))
        fobj.write(Border+"\n\n")

    fobj.write(Border+"\n\n")

    fobj.write(Border+"\n")
    fobj.write("---------------------End of Log File------------------------\n")
    fobj.write(Border+"\n")

def ProcessScan() :
    ListProcess = []

    print("Process Scan Report")

    # Warm up for CPU percent
    for proc in psutil.process_iter() :
        try :
            proc.cpu_percent()
        except :
            pass

    time.sleep(0.2)

    for proc in psutil.process_iter() :
        try : 
            info = proc.as_dict(attrs = ["pid" , "name" , "username", "status", "create_time","num_threads","open_files"])
            # Convert create_time
            try :
                info["create_time"] = time.strftime("%Y-%m-%d %H:%M%:%S",time.localtime(info["create_time"]))
            except:
                info["create_time"] = "NA"
            
            info["num_threads"] = proc.num_threads()
            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()
            info["open_files"] = len(proc.open_files())

            ListProcess.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            info["open_files"] = "Access Denied"   

    return ListProcess       

def main() :
    Border = "-"*60
    print(Border)
    print("----------Marvellous Platform Surveillance System-----------")
    print(Border)

    if(len(sys.argv) == 2) :
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H") :
            print("This script is used to ")
            print("1 : Create automatic logs")
            print("2 : Executes periodically")
            print("3 : Sends mail with the log")
            print("4 : Stores information about the processes")
            print("5 : Stores information about CPU")
            print("6 : Stores information about RAM usgae")
            print("7 : Stores information about secondary storage")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U") :
            print("Use the Automation as ")
            print("ScriptName.py TimeInterval DirectoryName")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("DirectoryName : Name of Directory to create auto logs")

        else :
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")

    # python Demo.py 5 Marvellous
    elif(len(sys.argv) == 3) :
        print("Inside Projects Logic")
        print("Time interval : ",sys.argv[1])
        print("DirectorName : ",sys.argv[2])

        # Apply the Scheduler
        schedule.every(int(sys.argv[1])).minutes.do(CreateLog, sys.argv[2])

        print("Marvellous Platform Surveillance System started successfully")
        print("Directory created with name : ",sys.argv[2])
        print("Time Interval in minutes : ",sys.argv[1])
        print("Press Ctrl + C to stop the execution")

        # Wait till Abort
        while(True) :
            schedule.run_pending()
            time.sleep(1)

    else :
        print("Invalid Number of Command Line Arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")

    print(Border)
    print("--------------Thank you for using our script----------------")
    print(Border)

if __name__ == "__main__" :
    main()