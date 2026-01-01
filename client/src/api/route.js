import api from './main';

export const authRoutes = {
  login: data => api.post('auth/login/', data),
  register: data => api.post('auth/signup/', data),
  refreshToken: data => api.post('auth/token/refresh/', data),
  logout: () => api.post('auth/logout/'),
  passwordReset: () => api.get('auth/reset/'),
};

export const userRoutes = {
  list: params => api.get('users/', { params }),
  retrieve: id => api.get(`users/${id}/`),
  create: data => api.post('users/', data),
  update: (id, data) => api.put(`users/${id}/`, data),
  partialUpdate: (id, data) => api.patch(`users/${id}/`, data),
  delete: id => api.delete(`users/${id}/`),
};

export const postRoutes = {
  list: params => api.get('posts/', { params }),
  retrieve: id => api.get(`posts/${id}/`),
  create: data => api.post('posts/', data),
  update: (id, data) => api.put(`posts/${id}/`, data),
  partialUpdate: (id, data) => api.patch(`posts/${id}/`, data),
  delete: id => api.delete(`posts/${id}/`),
};

export const commentRoutes = {
  list: postId => api.get(`posts/${postId}/comments/`),
  create: (postId, data) =>
    api.post(`posts/${postId}/comments/`, data),
  delete: (postId, commentId) =>
    api.delete(`posts/${postId}/comments/${commentId}/`),
};

export const uploadRoutes = {
  uploadImage: file => {
    const formData = new FormData();
    formData.append('image', file);

    return api.post('upload/', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    });
  },
};

export const searchRoutes = {
  searchPosts: query =>
    api.get('posts/', {
      params: { search: query },
    }),
};


export const adminRoutes = {
  stats: () => api.get('admin/'),
};
