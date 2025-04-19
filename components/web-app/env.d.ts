export interface Action {
  id: string;
  name: string;
  group_actor: string;
  description: string;
}

export interface Opinion {
  id: number;
  text: string;
  author: string;
  action_id: string;
}

export interface ActionResponse {
  id: number;
  name: string;
  group_actor: string;
  description: string;
  opinions?: Opinion[];
}
