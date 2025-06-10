import AsyncStorage from '@react-native-async-storage/async-storage';
import React, { createContext, useContext, useEffect, useState } from 'react';

const AuthContext = createContext();

export const useAuth = () => {
    const context = useContext(AuthContext);
    if (!context) {
        throw new Error('useAuth must be used within an AuthProvider');
    }
    return context;
};

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);
    const [token, setToken] = useState(null);
    const [loading, setLoading] = useState(true);

    // Check for existing token on app start
    useEffect(() => {
        checkAuthState();
    }, []);

    const checkAuthState = async () => {
        try {
            const storedToken = await AsyncStorage.getItem('userToken');
            const storedUser = await AsyncStorage.getItem('userData');
            
            if (storedToken && storedUser) {
                setToken(storedToken);
                setUser(JSON.parse(storedUser));
            }
        } catch (error) {
            console.error('Error checking auth state:', error);
        } finally {
            setLoading(false);
        }
    };

    const login = async (username, password) => {
        try {
            console.log('Attempting login with:', username);
            
            // Try multiple possible endpoints
            const possibleEndpoints = [
                'http://localhost:8000/auth/login/',
                'http://localhost:8000/api/auth/login/',
                'http://localhost:8000/api-token-auth/',
                'http://localhost:8000/login/'
            ];

            let response;
            let endpoint;
            
            for (endpoint of possibleEndpoints) {
                try {
                    console.log('Trying endpoint:', endpoint);
                    response = await fetch(endpoint, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ username, password }),
                    });
                    
                    if (response.status !== 404) {
                        console.log('Found working endpoint:', endpoint);
                        break;
                    }
                } catch (error) {
                    console.log('Endpoint failed:', endpoint, error.message);
                    continue;
                }
            }

            if (!response || response.status === 404) {
                throw new Error('No valid login endpoint found');
            }

            console.log('Login response status:', response.status);
            
            if (!response.ok) {
                const errorText = await response.text();
                console.log('Login error response:', errorText);
                
                let errorMessage = 'Login failed';
                try {
                    const errorData = JSON.parse(errorText);
                    errorMessage = errorData.message || errorData.detail || errorData.error || 'Login failed';
                } catch {
                    errorMessage = errorText || 'Login failed';
                }
                throw new Error(errorMessage);
            }

            const data = await response.json();
            console.log('Login success data:', data);
            
            // Handle different response formats
            let token, userData;
            
            if (data.token) {
                token = data.token;
                userData = data.user || { username };
            } else if (data.key) {
                // Some Django setups use 'key' instead of 'token'
                token = data.key;
                userData = data.user || { username };
            } else {
                throw new Error('No token received from server');
            }
            
            // Store token and user data
            await AsyncStorage.setItem('userToken', token);
            await AsyncStorage.setItem('userData', JSON.stringify(userData));
            
            setToken(token);
            setUser(userData);
            
            return { success: true };
        } catch (error) {
            console.error('Login error:', error);
            return { success: false, error: error.message };
        }
    };

    const register = async (username, email, password) => {
        try {
            console.log('Attempting registration with:', username, email);
            
            // Try multiple possible endpoints
            const possibleEndpoints = [
                'http://localhost:8000/auth/register/',
                'http://localhost:8000/api/auth/register/',
                'http://localhost:8000/register/'
            ];

            let response;
            let endpoint;
            
            for (endpoint of possibleEndpoints) {
                try {
                    console.log('Trying registration endpoint:', endpoint);
                    response = await fetch(endpoint, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ username, email, password }),
                    });
                    
                    if (response.status !== 404) {
                        console.log('Found working registration endpoint:', endpoint);
                        break;
                    }
                } catch (error) {
                    console.log('Registration endpoint failed:', endpoint, error.message);
                    continue;
                }
            }

            if (!response || response.status === 404) {
                throw new Error('No valid registration endpoint found');
            }

            console.log('Registration response status:', response.status);

            if (!response.ok) {
                const errorText = await response.text();
                console.log('Registration error response:', errorText);
                
                let errorMessage = 'Registration failed';
                try {
                    const errorData = JSON.parse(errorText);
                    errorMessage = errorData.message || errorData.detail || errorData.error || 'Registration failed';
                } catch {
                    errorMessage = errorText || 'Registration failed';
                }
                throw new Error(errorMessage);
            }

            const data = await response.json();
            console.log('Registration success data:', data);
            
            // Handle different response formats
            let token, userData;
            
            if (data.token) {
                token = data.token;
                userData = data.user || { username, email };
            } else if (data.key) {
                token = data.key;
                userData = data.user || { username, email };
            } else {
                // Some registration endpoints don't return a token immediately
                console.log('Registration successful, but no token returned. User may need to login.');
                return { success: true, needsLogin: true };
            }
            
            // Auto-login after registration if token received
            await AsyncStorage.setItem('userToken', token);
            await AsyncStorage.setItem('userData', JSON.stringify(userData));
            
            setToken(token);
            setUser(userData);
            
            return { success: true };
        } catch (error) {
            console.error('Registration error:', error);
            return { success: false, error: error.message };
        }
    };

    const logout = async () => {
        try {
            await AsyncStorage.removeItem('userToken');
            await AsyncStorage.removeItem('userData');
            setToken(null);
            setUser(null);
        } catch (error) {
            console.error('Logout error:', error);
        }
    };

    const value = {
        user,
        token,
        loading,
        login,
        register,
        logout,
        isAuthenticated: !!token,
    };

    return (
        <AuthContext.Provider value={value}>
            {children}
        </AuthContext.Provider>
    );
};