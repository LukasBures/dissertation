### kill process on GPU
```console
    nvidia-smi | grep 'python' | awk '{ print $5 }' | xargs -n1 kill -9
```

### enable persistence mode
```console
    sudo nvidia-smi -pm 1
```

### modification of GPU power consumption
```console
    sudo nvidia-smi -i 0 -pl 140 # 1080 
    sudo nvidia-smi -i 1 -pl 250 # 1080Ti
```

### 2TB disk mount point
```console
    cd /media/lukas/WD_2TB
```