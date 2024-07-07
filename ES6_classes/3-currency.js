export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  set code(newcode) {
    this._name = newcode;
  }

  get code() {
    return this._code;
  }

  set name(newname) {
    this._name = newname;
  }

  get name() {
    return this._name;
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
