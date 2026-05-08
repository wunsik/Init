import React, { useEffect, useState } from 'react'

export function InventoryPage() {
  const [data, setData] = useState(null)
  const [error, setError] = useState('')

  useEffect(() => {
    fetch('http://localhost:8000/api/v1/inventory')
      .then((r) => r.json())
      .then(setData)
      .catch(() => setError('Failed to load inventory'))
  }, [])

  if (error) return <p>{error}</p>
  if (!data) return <p>Loading inventory…</p>

  return (
    <main>
      <h1>Inventory Snapshot</h1>
      <ul>
        {data.items.map((item) => (
          <li key={item.sku}>{item.sku} — {item.quantity} @ {item.warehouse}</li>
        ))}
      </ul>
    </main>
  )
}
