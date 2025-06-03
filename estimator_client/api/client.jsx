// const API_BASE_URL = process.env.EXPO_PUBLIC_API_URL || 'http://localhost:3000/api';

// class ApiClient {
//   constructor() {
//     this.baseURL = API_BASE_URL;
//   }

//   async request(endpoint, options = {}) {
//     const url = `${this.baseURL}${endpoint}`;
//     const config = {
//       headers: {
//         'Content-Type': 'application/json',
//         ...options.headers,
//       },
//       ...options,
//     };

//     // Add auth token if available
//     const token = await this.getAuthToken();
//     if (token) {
//       config.headers.Authorization = `Bearer ${token}`;
//     }

//     try {
//       const response = await fetch(url, config);
      
//       if (!response.ok) {
//         throw new Error(`HTTP error! status: ${response.status}`);
//       }
      
//       return await response.json();
//     } catch (error) {
//       console.error('API request failed:', error);
//       throw error;
//     }
//   }

//   async getAuthToken() {
//     // Implement your token storage logic here
//     // e.g., AsyncStorage, SecureStore, etc.
//     return null;
//   }

//   // HTTP methods
//   get(endpoint, options = {}) {
//     return this.request(endpoint, { ...options, method: 'GET' });
//   }

//   post(endpoint, data, options = {}) {
//     return this.request(endpoint, {
//       ...options,
//       method: 'POST',
//       body: JSON.stringify(data),
//     });
//   }

//   put(endpoint, data, options = {}) {
//     return this.request(endpoint, {
//       ...options,
//       method: 'PUT',
//       body: JSON.stringify(data),
//     });
//   }

//   delete(endpoint, options = {}) {
//     return this.request(endpoint, { ...options, method: 'DELETE' });
//   }
// }

// export default new ApiClient();