import React from "react"
import { NavLink } from "react-router-dom"

const NavBar: React.FC = () => {
  return (
    <nav className="p-4">
      <ul className="flex">
        <li className="mr-6">
          <NavLink to="/" className="text-white">
            Home
          </NavLink>
        </li>
        <li>
          <NavLink to="/chat" className="text-white">
            Chat
          </NavLink>
        </li>
      </ul>
    </nav>
  )
}

export default NavBar
