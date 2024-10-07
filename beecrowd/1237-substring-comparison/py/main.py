def main():
  # TODO: Solve this with Dynamic Programming

  while True:
    try:
      s2_dict = {}
      s1 = input()
      s2 = input()

      for index, char in enumerate(s2):
        if char in s2_dict:
          s2_dict[char].append(index)
        else:
          s2_dict[char] = [index]
      
      i = 0
      j = 0
      k = 0
      longest_substring = 0
      while i < len(s1):
        if s1[i] in s2_dict:
          for s2_index in s2_dict[s1[i]]:
            j = i
            k = s2_index
            substring_size = 0
            while j < len(s1) and k < len(s2) and s1[j] == s2[k]:
                substring_size += 1
                j += 1
                k += 1
            if substring_size > longest_substring:
                longest_substring = substring_size
        i += 1
      print(longest_substring)
    except EOFError:
      break

if __name__ == "__main__":
  main()