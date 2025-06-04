import React, { useEffect, useState } from 'react'
import { StyleSheet, Text, View } from 'react-native'
import { FlatList } from 'react-native-web'

const Items = () => {
    const [libraries, setLibraries] = useState([])
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        fetchLibraries()
    }, [])

    const fetchLibraries = async () => {
        try {
            const response = await fetch('http://localhost:8000/libraries', {
                headers: {
                    Authorization: `Token 1a5908171df05b095338c23f9bb5ee7154f8c11c`
                }
            }) 
            const data = await response.json()
            setLibraries(data)
        } catch (error) {
            console.error('Error fetching libraries:', error)
        } finally {
            setLoading(false)
        }
    }

    if (loading) {
        return (
            <View style={styles.container}>
                <Text style={styles.text}>Loading...</Text>
            </View>
        )
    }

    return (
        <View style={styles.container}>
            <Text style={styles.text}>Items/Services</Text>
            <FlatList
                data={libraries}
                keyExtractor={(item) => item.id.toString()}
                renderItem={({ item }) => (
                    <View style={styles.libraryItem}>
                        <Text style={styles.libraryName}>{item.name}</Text>
                        <Text style={styles.libraryDescription}>{item.description}</Text>
                    </View>
                )}
                style={styles.list}
            />
        </View>
    )
}

export default Items

const styles = StyleSheet.create({
    container: {
        flex: 1,
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
    },
    text: {
        color: 'grey',
        fontSize: 42,
        fontWeight: 'bold',
        textAlign: 'center'
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
    },
    libraryItem: {
        backgroundColor: '#f5f5f5',
        padding: 15,
        marginVertical: 5,
        borderRadius: 8,
    },
    libraryName: {
        fontSize: 16,
        fontWeight: 'bold',
    },
    libraryDescription: {
        fontSize: 14,
        color: '#666',
        marginTop: 4,
    }
})