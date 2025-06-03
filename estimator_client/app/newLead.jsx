import { router } from 'expo-router';
import React, { useState } from 'react';
import {
    Alert,
    ScrollView,
    StyleSheet,
    Text,
    TextInput,
    TouchableOpacity,
    View
} from 'react-native';

export default function NewLead() {
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    city: '',
    state: '',
    address: '',
    phone: '',
    notes: '',
    howDidYouHear: ''
  })

  const states = [
    'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
    'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
    'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
    'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
    'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
  ]

  const updateField = (field, value) => {
    setFormData(prev => ({
      ...prev,
      [field]: value
    }))
  }

  const handleAddToLeads = async () => {
    // Basic validation
    if (!formData.firstName || !formData.lastName) {
      Alert.alert('Error', 'First and Last name are required')
      return
    }

    try {
      // Replace with your actual API endpoint
      const response = await fetch('YOUR_API_URL/leads', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
      })

      if (response.ok) {
        Alert.alert('Success', 'Lead added successfully!', [
          { text: 'OK', onPress: () => router.back() }
        ])
      } else {
        Alert.alert('Error', 'Failed to add lead')
      }
    } catch (error) {
      console.error('Error adding lead:', error)
      Alert.alert('Error', 'Something went wrong')
    }
  }

  return (
    <ScrollView style={styles.container}>
      <View style={styles.header}>
        <TouchableOpacity onPress={() => router.back()} style={styles.backButton}>
          <Text style={styles.backArrow}>‹</Text>
        </TouchableOpacity>
        <Text style={styles.title}>New Client</Text>
      </View>

      <Text style={styles.sectionTitle}>Contact</Text>

      <View style={styles.form}>
        <View style={styles.row}>
          <TextInput
            style={[styles.input, styles.halfInput]}
            placeholder="First"
            value={formData.firstName}
            onChangeText={(text) => updateField('firstName', text)}
          />
          <TextInput
            style={[styles.input, styles.halfInput]}
            placeholder="Last"
            value={formData.lastName}
            onChangeText={(text) => updateField('lastName', text)}
          />
        </View>

        <View style={styles.row}>
          <TextInput
            style={[styles.input, styles.halfInput]}
            placeholder="City"
            value={formData.city}
            onChangeText={(text) => updateField('city', text)}
          />
          <TextInput
            style={[styles.input, styles.halfInput]}
            placeholder="State"
            value={formData.state}
            onChangeText={(text) => updateField('state', text)}
          />
        </View>

        <TextInput
          style={styles.input}
          placeholder="Address"
          value={formData.address}
          onChangeText={(text) => updateField('address', text)}
        />

        <TextInput
          style={styles.input}
          placeholder="Phone"
          value={formData.phone}
          onChangeText={(text) => updateField('phone', text)}
          keyboardType="phone-pad"
        />

        <TextInput
          style={[styles.input, styles.textArea]}
          placeholder="Notes"
          value={formData.notes}
          onChangeText={(text) => updateField('notes', text)}
          multiline
          numberOfLines={3}
        />

        <Text style={styles.label}>How did you hear from us?</Text>
        <TextInput
          style={styles.input}
          placeholder="Business card"
          value={formData.howDidYouHear}
          onChangeText={(text) => updateField('howDidYouHear', text)}
        />

        <TouchableOpacity style={styles.addButton} onPress={handleAddToLeads}>
          <Text style={styles.addButtonText}>Add Client to leads</Text>
        </TouchableOpacity>
      </View>
    </ScrollView>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    padding: 20,
    backgroundColor: 'white',
  },
  backButton: {
    marginRight: 15,
  },
  backArrow: {
    fontSize: 24,
    fontWeight: 'bold',
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'center',
    marginVertical: 20,
    color: '#333',
  },
  form: {
    backgroundColor: 'white',
    padding: 20,
    margin: 10,
    borderRadius: 10,
  },
  row: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 15,
  },
  input: {
    borderWidth: 1,
    borderColor: '#ddd',
    borderRadius: 8,
    padding: 15,
    fontSize: 16,
    backgroundColor: 'white',
    marginBottom: 15,
  },
  halfInput: {
    flex: 0.48,
    marginBottom: 0,
  },
  textArea: {
    height: 80,
    textAlignVertical: 'top',
  },
  pickerContainer: {
    justifyContent: 'center',
    paddingHorizontal: 5,
  },
  picker: {
    height: 50,
  },
  label: {
    fontSize: 16,
    fontWeight: '500',
    marginBottom: 10,
    color: '#333',
  },
  addButton: {
    backgroundColor: '#4CAF50',
    padding: 15,
    borderRadius: 8,
    alignItems: 'center',
    marginTop: 20,
  },
  addButtonText: {
    color: 'white',
    fontSize: 16,
    fontWeight: 'bold',
  },
})