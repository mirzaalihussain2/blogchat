import React from "react"
import { NavLink } from "react-router-dom"

const NavBar: React.FC = () => {
  return (
    <nav>
      <ul>
        <li>
          <NavLink to="/">Home</NavLink>
        </li>
        <li>
          <NavLink to="/chat">Chat</NavLink>
        </li>
      </ul>
    </nav>
  )
}

export default NavBar
