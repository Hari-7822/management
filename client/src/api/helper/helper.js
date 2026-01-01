import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import api from './client';

export const fetchTodos = async () => {
  const { data } = await api.get('todos/');
  return data;
};

export const createTodo = async (newTodo) => {
  const { data } = await api.post('todos/', newTodo);
  return data;
};

export const deleteTodo = async (id) => {
  await api.delete(`todos/${id}/`);
  return id;
};

export const useTodos = () => {
  return useQuery({
    queryKey: ['todos'],
    queryFn: fetchTodos,
  });
};

export const useCreateTodo = () => {
  const queryClient = useQueryClient();

  return useMutation(createTodo, {
    onSuccess: () => {
      queryClient.invalidateQueries(['todos']);
    },
  });
};

export const useDeleteTodo = () => {
  const queryClient = useQueryClient();

  return useMutation(deleteTodo, {
    onSuccess: (id) => {
      queryClient.invalidateQueries(['todos']);
    },
  });
};
