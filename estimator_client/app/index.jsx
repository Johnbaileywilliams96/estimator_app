// import { router } from 'expo-router';
// import { useEffect } from 'react';
// import LoadingView from '../components/LoadingView';
// import { useAuth } from '../contexts/AuthContext';

// export default function Index() {
//     const { isAuthenticated, loading } = useAuth();

//     useEffect(() => {
//         if (!loading) {
//             if (isAuthenticated) {
//                 // User is logged in, go to main app
//                 router.replace('/(tabs)');
//             } else {
//                 // User is not logged in, go to login
//                 router.replace('/(auth)/login');
//             }
//         }
//     }, [isAuthenticated, loading]);

//     // Show loading while checking authentication
//     return <LoadingView message="Checking authentication..." />;
// }