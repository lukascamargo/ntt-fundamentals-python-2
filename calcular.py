def exec(A,B):
  for contador in range(1, A + 1):
    C = contador + B
    print('{} + {} = {}'.format(contador, B, C))
  
    if (contador <= 10):
      continue
    else:
      break
