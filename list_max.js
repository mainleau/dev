list_max = ([a, ...b]) => {
  return !b.length ? a : a > list_max(b) ? a : list_max(b);
}

list_max = ([ a, ...b ] , c = a) => {
  return !a ? c : list_max(b, a > c ? a : c);
}
