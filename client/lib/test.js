const HORNER_FLAT_LISTS = Object.entries();

const object = {
  a: "Jesus is LORD",
  b: 365,
};

for (const [key, value] of Object.entries(object)) {
  console.log(`${key} : ${value}`);
}
