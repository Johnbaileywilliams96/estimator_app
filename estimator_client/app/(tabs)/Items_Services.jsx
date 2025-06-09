import React from 'react';
import { FlatList, StyleSheet, Text, View } from 'react-native';
import LibraryItem from '../../components/LibraryItem';
import LoadingView from '../../components/LoadingView';
import { useLibraries } from '../../hooks/useLibraries';

const Items = () => {
    const { libraries, loading, error } = useLibraries();

    if (loading) return <LoadingView />;
    
    if (error) return <LoadingView message={`Error: ${error}`} />;

    return (
        <View style={styles.container}>
            <Text style={styles.title}>Items/Services</Text>
            <FlatList
                data={libraries}
                keyExtractor={(item) => item.id.toString()}
                renderItem={({ item }) => <LibraryItem item={item} />}
                style={styles.list}
            />
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
    },
    title: {
        fontSize: 24,
        fontWeight: 'bold',
        marginBottom: 20,
        color: 'grey'
    },
    list: {
        flex: 1,
        width: '100%',
    }
});

export default Items;