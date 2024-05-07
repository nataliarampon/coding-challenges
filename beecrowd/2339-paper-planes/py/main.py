if __name__ == '__main__':
  competitors, total_sheets, sheets_per_competitor = map(int, input().split())
  print('S' if sheets_per_competitor * competitors <= total_sheets else 'N')