import axios from "axios"
import { Character } from "./types"

// Fetch all characters
export function fetchAllCharacters(): Promise<Character[]> {
  return axios
    .get("/characters")
    .then((response) => response.data)
    .catch((error) => {
      // Handle error
      throw error
    })
}

// Create a character
export async function createCharacter(character: Omit<Character, "id">) {
  return axios
    .post("/characters", character)
    .then((response) => response.data)
    .catch((error) => {
      // Handle error
      throw error
    })
}

// Send a message to the chatbot
export function sendMessageToChatbot(message: string): Promise<string> {
  return axios
    .post("/chatbot", { message })
    .then((response) => response.data)
    .catch((error) => {
      // Handle error
      throw error
    })
}
