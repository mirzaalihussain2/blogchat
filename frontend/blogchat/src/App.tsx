import { useState } from "react"
import "./App.css"
import { BrowserRouter as Router, Route, Routes } from "react-router-dom"
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
      <Routes>
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
      </Routes>
    </Router>
  )
}

export default App
