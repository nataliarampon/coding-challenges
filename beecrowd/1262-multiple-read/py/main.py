def calculateMachineCycles(batch, processors):
  if batch[0] == 'R':
    return len(batch) // processors + (1 if len(batch) % processors != 0 else 0)
  else:
    return len(batch)

def main():
  while True:
    try:
      trace = input()
      parallel_processors = int(input())
      last_op = None
      op_batch = ''
      machine_cycles = 0

      for op in trace:
        if op == last_op or last_op == None:
          op_batch += op
        else:
            machine_cycles += calculateMachineCycles(op_batch, parallel_processors)
            op_batch = op
        last_op = op
      machine_cycles += calculateMachineCycles(op_batch, parallel_processors)
      print(machine_cycles)
    except EOFError:
      break

if __name__ == "__main__":
  main()