import React, { useState } from "react"
import NavBar from "../nav/nav"
import { Character } from "../api/types"

interface ChatMessage {
  id: number
  text: string
  isUser: boolean
}

interface Props {
  selectedCharacter: Character | undefined
}

const ChatbotInterface = ({ selectedCharacter }: Props) => {
  const [messages, setMessages] = useState<ChatMessage[]>([])
  const [inputText, setInputText] = useState("")

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setInputText(e.target.value)
  }

  const handleSendMessage = () => {
    if (inputText.trim() !== "") {
      const newMessage: ChatMessage = {
        id: messages.length + 1,
        text: inputText,
        isUser: true,
      }

      setMessages([...messages, newMessage])
      setInputText("")
    }
  }

  return (
    <div>
      <NavBar />
      <div>
        <div>
          {messages.map((message) => (
            <div key={message.id}>
              {message.isUser ? (
                <div>{message.text}</div>
              ) : (
                <div>Chatbot: {message.text}</div>
              )}
            </div>
          ))}
        </div>
        <div>
          <input type="text" value={inputText} onChange={handleInputChange} />
          <button onClick={handleSendMessage}>Send</button>
        </div>
      </div>
    </div>
  )
}

export default ChatbotInterface
