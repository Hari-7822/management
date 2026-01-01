import axios from 'axios';

const api = axios.create({
  baseURL: 'http://192.168.29.240:8000/api/',
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
  },
});

api.interceptors.request.use(async config => {
  const token = global.authToken; 
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;
