def main():
    steps = int(input())
    up = list(map(int, input().split()))
    down = list(map(int, input().split()))

    # we need to find the best between starting up or down
    changes = min(simulate_level(steps, up, down), simulate_level(steps, down, up))
    print(changes)

def simulate_level(steps, start_layer, second_layer):
    layers = [start_layer, second_layer]
    changes = 0
    for i in range(steps-1):
        if layers[changes % 2][i] == 0:
            changes = steps
            break
        else:
            if layers[changes % 2][i+1] == 0 or layers[changes % 2][i+1] > layers[changes % 2][i]:
                changes += 1
    return changes

if __name__ == "__main__":
    main()