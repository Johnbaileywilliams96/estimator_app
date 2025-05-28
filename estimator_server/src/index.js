import express from 'express'
import { PrismaClient } from '@prisma/client'

const app = express()
const prisma = new PrismaClient()

app.use(express.json())

app.get('/clients', async (req, res) => {
  const clients = await prisma.client.findMany()
  res.json(clients)
})

app.listen(3000, () => {
  console.log('🚀 Server is running on http://localhost:3000')
})
