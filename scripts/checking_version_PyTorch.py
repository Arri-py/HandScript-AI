import torch
import time

def print_separator(title):
    print(f"\n{'=' * 50}")
    print(f"|| {title:^44} ||")
    print(f"{'=' * 50}")

# ======================== БАЗОВАЯ ИНФОРМАЦИЯ ========================
print_separator("PyTorch & CUDA Info")

print(f"{'PyTorch version:':<25} {torch.__version__}")
print(f"{'CUDA available:':<25} {torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"{'CUDA version:':<25} {torch.version.cuda}")
    print(f"{'GPU device name:':<25} {torch.cuda.get_device_name(0)}")
    print(f"{'GPU device count:':<25} {torch.cuda.device_count()}")
    print(f"{'Current device:':<25} {torch.cuda.current_device()}")
    print(f"{'cuDNN enabled:':<25} {torch.backends.cudnn.enabled}")
    print(f"{'cuDNN version:':<25} {torch.backends.cudnn.version()}")
else:
    print("CUDA is NOT available")

# ======================== ТЕСТ ПАМЯТИ GPU ========================
if torch.cuda.is_available():
    print_separator("GPU Memory Test")
    
    total_mem = torch.cuda.get_device_properties(0).total_memory / (1024**3)
    free_mem = torch.cuda.memory_reserved(0) / (1024**3)
    
    print(f"{'Total GPU Memory:':<25} {total_mem:.2f} GB")
    print(f"{'Free GPU Memory:':<25} {free_mem:.2f} GB")

# ======================== ТЕСТ ТЕНЗОРОВ ========================
print_separator("Tensor Operations Test")

# Создаем тестовые тензоры
x_cpu = torch.rand(5000, 5000)
if torch.cuda.is_available():
    x_gpu = x_cpu.to('cuda')

print(f"{'CPU tensor size:':<25} {x_cpu.size()}")
if torch.cuda.is_available():
    print(f"{'GPU tensor size:':<25} {x_gpu.size()}")

# ======================== ТЕСТ ПРОИЗВОДИТЕЛЬНОСТИ ========================
if torch.cuda.is_available():
    print_separator("Performance Benchmark")
    
    # Включаем автоматическую оптимизацию
    torch.backends.cudnn.benchmark = True
    
    # Тест матричного умножения
    a = torch.randn(10000, 10000, device='cuda')
    b = torch.randn(10000, 10000, device='cuda')
    
    # Прогрев GPU
    for _ in range(5):
        _ = torch.matmul(a, b)
    
    # Точный замер времени
    start_time = time.time()
    _ = torch.matmul(a, b)
    gpu_time = time.time() - start_time
    
    # Тест на CPU для сравнения
    a_cpu = a.cpu()
    b_cpu = b.cpu()
    
    start_time = time.time()
    _ = torch.matmul(a_cpu, b_cpu)
    cpu_time = time.time() - start_time
    
    print(f"{'GPU matmul (10000x10000):':<25} {gpu_time * 1000:.2f} ms")
    print(f"{'CPU matmul (10000x10000):':<25} {cpu_time * 1000:.2f} ms")
    print(f"{'Speedup (GPU vs CPU):':<25} {cpu_time / gpu_time:.1f}x")

# ======================== ДОПОЛНИТЕЛЬНЫЕ ТЕСТЫ ========================
if torch.cuda.is_available():
    print_separator("Advanced Tests")
    
    # Тест памяти
    large_tensor = torch.zeros(int(1e8), dtype=torch.float32, device='cuda')
    print(f"{'Allocated 100M elements:':<25} {large_tensor.size(0)//int(1e6)}M elements")
    
    # Тест операций
    start = time.time()
    _ = torch.fft.fft(large_tensor)
    fft_time = time.time() - start
    print(f"{'FFT operation time:':<25} {fft_time * 1000:.2f} ms")

print_separator("TEST COMPLETED")