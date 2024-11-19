import numpy as np

def calculate(numbers: list) -> dict:
    
    #check len of list to ensure it has 9 numbers
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers")
    
    #convert list to a numpy array
    numbers = np.array(numbers).reshape(3,3)
    
    #calculate mean, variance, standard deviation, max, min, and sum
    
    result = {
        "mean": [
            numbers.mean(axis=0).tolist(),
            numbers.mean(axis=1).tolist(),
            numbers.mean().item()
        ],
        "variance": [
            numbers.var(axis=0).tolist(),
            numbers.var(axis=1).tolist(),
            numbers.var().item()
        ],
        "standard deviation": [
            numbers.std(axis=0).tolist(),
            numbers.std(axis=1).tolist(),
            numbers.std().item()
        ],
        "max": [
            numbers.max(axis=0).tolist(),
            numbers.max(axis=1).tolist(),
            numbers.max().item()
        ],
        "min": [
            numbers.min(axis=0).tolist(),
            numbers.min(axis=1).tolist(),
            numbers.min().item()
        ],
        "sum": [
            numbers.sum(axis=0).tolist(),
            numbers.sum(axis=1).tolist(),
            numbers.sum().item()
        ]
    }
    
    return result

output = calculate([7,2,14,27,3,12,10,21,15])
print(output)