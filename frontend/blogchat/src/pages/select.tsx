import React, { useEffect, useState } from "react"
import NavBar from "../nav/nav"
import { createCharacter, fetchAllCharacters } from "../api/requests"
import { Character } from "../api/types"

interface Props {
  selectedCharacter: Character | undefined
  setSelectedCharacter: (character: Character) => void
}

const CharacterSelectionPage = ({
  selectedCharacter,
  setSelectedCharacter,
}: Props) => {
  const [characters, setCharacters] = useState<Character[]>([])
  const [name, setName] = useState<string>("")
  const [description, setDescription] = useState<string>("")
  const [sourceUrl, setSourceUrl] = useState<string>("")

  useEffect(() => {
    async function fetchCharacters() {
      const characters = await fetchAllCharacters()
      setCharacters(characters)
    }

    // fetchCharacters()
  }, [])

  const loading = characters.length === 0

  const handleNameChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setName(event.target.value)
  }

  const handleDescriptionChange = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    setDescription(event.target.value)
  }

  const handleSourceUrlChange = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    setSourceUrl(event.target.value)
  }

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault()
    try {
      const newCharacter = await createCharacter({
        name,
        description,
        source_url: sourceUrl,
      })
      setCharacters([...characters, newCharacter])
      setName("")
      setDescription("")
      setSourceUrl("")
    } catch (error) {
      console.error("Error creating character:", error)
    }
  }

  return (
    <div>
      <NavBar />
      <h1>Character Selection</h1>
      <div className="character-list">
        {loading && <div>Loading...</div>}
        {characters.map((character) => (
          <div
            key={character.id}
            className="character-card"
            onClick={() => setSelectedCharacter(character)}
          >
            <img src={character.source_url} alt={character.name} />
            <h2>{character.name}</h2>
          </div>
        ))}
      </div>
      <div className="add-character">
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            placeholder="Enter character name"
            value={name}
            onChange={handleNameChange}
          />
          <input
            type="text"
            placeholder="Enter character description"
            value={description}
            onChange={handleDescriptionChange}
          />
          <input
            type="text"
            placeholder="Enter character source URL"
            value={sourceUrl}
            onChange={handleSourceUrlChange}
          />
          <button>Add Character</button>
        </form>
      </div>
    </div>
  )
}

export default CharacterSelectionPage
