import psutil

def get_mem_data():    
    data = psutil.virtual_memory()
    return {
        'free_mem': data.available,
        'total_mem': data.total,
        'in_use_mem': data.used,
        'mem_per': data.percent
    }

def main():
    mem_data =  get_mem_data()
    print(f"Memory Info: {mem_data}")

if __name__ == "__main__":
    main()
