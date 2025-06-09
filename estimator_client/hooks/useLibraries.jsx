import { useEffect, useState } from 'react';

export const useLibraries = () => {
    const [libraries, setLibraries] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    const fetchLibraries = async () => {
        try {
            setLoading(true);
            const response = await fetch('http://localhost:8000/libraries', {
                headers: {
                    Authorization: `Token 1a5908171df05b095338c23f9bb5ee7154f8c11c`
                }
            });
            
            if (!response.ok) throw new Error('Failed to fetch libraries');
            
            const data = await response.json();
            setLibraries(data);
            setError(null);
        } catch (err) {
            console.error('Error fetching libraries:', err);
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchLibraries();
    }, []);

    return { libraries, loading, error, refetch: fetchLibraries };
};