import { useState } from "react"
import reactLogo from "./assets/react.svg"
import viteLogo from "/vite.svg"
import "./App.css"
import { BrowserRouter as Router, Switch, Route } from "react-router-dom"
import Home from "../src/pages/select"
import Chat from "../src/pages/chat"
import { Character } from "./api/types"

function App() {
  // Pass down instead of using context (for ease)
  const [selectedCharacter, setSelectedCharacter] = useState<
    Character | undefined
  >(undefined)

  return (
    <Router>
      <Switch>
        <Route
          path="/"
          element={
            <Home
              selectedCharacter={selectedCharacter}
              setSelectedCharacter={setSelectedCharacter}
            />
          }
        />
        <Route
          path="/chat"
          element={<Chat selectedCharacter={selectedCharacter} />}
        />
      </Switch>
    </Router>
  )
}

export default App
