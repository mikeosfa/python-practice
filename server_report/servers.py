import csv
from datetime import datetime, timedelta
import config

def load_servers(filename):
    """Load server data from CSV into a list of dictionaries."""
    
    servers = []

    try:

        with open(filename, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
        
            for row in reader:
                servers.append(row)
    except FileNotFoundError:
        print(f"Could not find file: {filename}")
        return []

    except PermissionError:
        print(f"No permission to read: {filename}")
        return []  
    
    return servers

def total_servers (servers):
    return len(servers)

def grouped_environments (servers):
    envs = {}
    for row in servers:
        environment = row["environment"]
        
    
        if environment not in envs:
            envs[environment] = 0

        envs[environment] += 1
    
    return envs

def grouped_os (servers):
    os_summary = {}
    for row in servers:
        operating_system = row["os"]
            
        
        if operating_system not in os_summary:
            os_summary[operating_system] = 0
    
        os_summary[operating_system] += 1
        
    return os_summary

def patching_required (servers, patch_days):
    cut_off_date = datetime.today() - timedelta(days=patch_days)
    patching_list = []
    for row in servers:
        patch_date = datetime.strptime(row["patch_date"], "%Y-%m-%d")

        if patch_date < cut_off_date:
            patching_list.append({
                "hostname": row["hostname"],
                 "patch_date": row["patch_date"]
            })
    return patching_list

def average_memory_use (servers):
    total = 0
    for row in servers:
        total += float(row["memory"])
    average = total / len(servers)
    return average


def main():

    
    servers = load_servers(config.CSV_PATH)

    if not servers:
        print("No server data loaded. Exiting.")
        return

    total = total_servers(servers)
    environments = grouped_environments(servers)
    operating_systems = grouped_os(servers)
    servers_need_patching = patching_required(servers, config.PATCH_DAYS)
    average_memory = average_memory_use(servers)

    print("\nInfrastructure Report")
    print("=====================")
    print(f"\nTotal servers: {total}")
    print("\nBy environment:")
    for env, count in environments.items():
        print(f"{env}: {count}")
    print("\nBy operating system:")
    for os, count in operating_systems.items():
        print(f"{os}: {count}")
    print("\nServers requiring patching:")
    for row in servers_need_patching:
        days_ago = datetime.today() - datetime.strptime(row["patch_date"], "%Y-%m-%d") 
        print(
            f"{row['hostname']}: patch date: {row['patch_date']}) "
            f"Last Patched {days_ago.days} days ago"
        )

    print("\nAverage memory:")
    print(f"{average_memory:.2f}GB")



if __name__ == "__main__":
    main()