const fs = require('fs')
const path = require('path')
const diff = require('./diff')


const first_signal = JSON.parse(fs.readFileSync(path.resolve(__dirname, 'second_signal.txt'), 'utf8'))

const az = ` !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_\`abcdefghijklmnopqrstuvwxyz{|}~`


const levenstein = (a, b) => diff.diff(a, b).levenshteinDistance


const clacDist = (a, b) => levenstein(a.join(''), '00000000'.substr(b.charCodeAt(0).toString(2).length) + b.charCodeAt(0).toString(2))


const getClosestToNeighbors = (arr) => {
  const counter = []

  az.split('').forEach((letter, i) => {
    arr.forEach(element => {
      const dist = clacDist(element, letter)
      counter[i] ? counter[i] += dist : counter[i] = dist
    })
  })
  const minValue = Math.min(...counter)
  const solve = {}
  counter.forEach((e, i) => {
    if (e === minValue) solve[i] = az[i]
  })
  return solve
}

const a = first_signal.map(e => getClosestToNeighbors(e))

console.log(a)
