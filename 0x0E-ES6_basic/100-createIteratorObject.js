export default function createIteratorObject(report) {
  let iterable = [];

  if (!report.allEmployees || typeof report.allEmployees !== 'object') {
    return iterable;
  }

  //   for (const r of Object.values(report.allEmployees)) {
  //     iterable.push(...r);
  //   }

  iterable = {
    * [Symbol.iterator]() {
      for (const value of Object.values(report.allEmployees)) {
        for (const i of value) {
          yield i;
        }
      }
    },
  };

  return iterable;
}
