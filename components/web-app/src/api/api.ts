import axios from 'axios';
import type {Action, ActionResponse, Opinion} from "../../env";

const api = axios.create({
  //@ts-expect-error ts doesnt know meta.env
  baseURL: import.meta.env.VITE_BACKEND_API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const createAction = async (actionData: Omit<Action, 'id'>): Promise<Action> => {
  try {
    const response = await api.post<Action>('/action/', actionData);
    return response.data;
  } catch (error) {
    console.error('Error creating action:', error);
    throw error;
  }
};

export const getOpinionsByAction = async (actionId: string): Promise<ActionResponse> => {
  try {
    const response = await api.get<ActionResponse>(`/opinion/action/${actionId}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching opinions:', error);
    throw error;
  }
};

export const createOpinion = async (opinionData: Omit<Opinion, 'id'>): Promise<Opinion> => {
  try {
    const response = await api.post<Opinion>('/opinion/', opinionData);
    return response.data;
  } catch (error) {
    console.error('Error creating opinion:', error);
    throw error;
  }
};
