export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const dataView = new DataView(buffer);
  const intView = new Int8Array(buffer);

  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }
  intView[position] = value;
  return dataView;
}
