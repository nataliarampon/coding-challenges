export function timeRequiredToBuy(tickets: number[], k: number): number {
    
  let time = 0;
  let i = 0;
  const queueLength = tickets.length;

  while (tickets[k] != 0) {
    if (tickets[i%queueLength] > 0) {
      time++;
      tickets[i%queueLength]--;
    }
    i++;
  }
  return time;
}