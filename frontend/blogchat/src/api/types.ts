export type Character = {
  id: string
  name: string
  description: string
  source_url: string
}

export type Blog = {
  id: string
  character_id: string
  title: string
  content: string
}
