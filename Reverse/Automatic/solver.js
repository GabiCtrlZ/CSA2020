const fs = require('fs')
const path = require('path')

const text = fs.readFileSync(path.resolve(__dirname, 'loops.txt'), 'utf8')

const data = text.split('\n')

const answerDict = {}

const MIN = 33
const MAX = 126

const findNumber = (arr) => {
  let num = MIN
  const dividers = [...arr]
  for (let i = MIN; i <= MAX; i += 1) {
    const ans = dividers.find((e) => {
      if (e < 0) {
        if ((num % (-e)) !== 0) return true
        num = Math.floor(num / (-e))
        return false
      }
      if ((num % e) === 0) return true
      return false
    })
    if (!ans) return i
    num = i + 1
  }
  return null
}

data.forEach((e) => {
  const [arrG1, g1, g2, g7] = e.split(',')

  if (!answerDict[parseInt(g1, 10)]) {
    answerDict[parseInt(g1, 10)] = []
  }

  if ((parseInt(g7, 10) !== 4) && (parseInt(g7, 10) !== 3)) return

  const s = (parseInt(g7, 10) === 4) ? -parseInt(g2, 10) : parseInt(g2, 10)

  answerDict[parseInt(g1, 10)].push(s)
})

console.log(Object.keys(answerDict).map((curr) => (String.fromCharCode(findNumber(answerDict[curr])))).join(''))
