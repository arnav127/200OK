import { useState, useEffect } from 'react'
import { useRouter } from 'next/router'
import Link from 'next/link'

import Layout from '../../components/Hospital/Layout'
import { useAuth } from '../../lib/auth'

const Dashboard = () => {
  const [isLoading, setIsLoading] = useState(true)
  const router = useRouter()

  useEffect(() => {
    const loadUser = () => {
      const isAuthenticated = localStorage.getItem('user')
      if (!isAuthenticated) router.replace('/hospital/login')
    }
    loadUser()
    setIsLoading(false)
  }, [])

  return isLoading ? (
    'Loading...'
  ) : (
    <Layout title="Dashboard">
      <div className="grid grid-cols-3 gap-4">
        <div className="flex h-36 flex-col justify-between rounded-lg bg-green-100/50 p-4 text-center text-green-800 shadow-md">
          <h4 className="order-1 self-start font-semibold uppercase">
            Patients
          </h4>
          <p className="order-0 flex self-end text-4xl">
            <span className="font-bold">420</span>
            <span>/</span>
            <span className="font-bold">6969</span>
          </p>
        </div>
        <div className="h-36 rounded-lg bg-gray-100/50 p-4 text-center shadow-md">
          Value
        </div>
        <div className="rounded-lg bg-blue-100/50 text-blue-800 shadow-md">
          <Link href="/hospital/admit" as="a">
            <h4 className="flex h-36 cursor-pointer items-center justify-between p-4">
              Admit Patient
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-24 w-24 self-center"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M12 9v3m0 0v3m0-3h3m-3 0H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z"
                />
              </svg>
            </h4>
          </Link>
        </div>
        <div className="col-span-2">
          <h2 className="font-semibold uppercase">Patient Records</h2>
        </div>
        <div>
          <h2 className="font-semibold uppercase">Resources</h2>
        </div>
      </div>
    </Layout>
  )
}

export default Dashboard
