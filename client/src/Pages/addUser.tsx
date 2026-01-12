import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, Alert, ScrollView } from 'react-native';
import { useMutation } from '@tanstack/react-query';
import axios from 'axios';

const url = 'http://localhost:8000/api/users/';

const AddUser = () => {
  const [d, setD] = useState({ u: '', e: '', p: '', f: '', l: '' });
  const [err, setErr] = useState('');

  const mut = useMutation({
    mutationFn: (fd) => axios.post(url, fd),
    onSuccess: () => {
      Alert.alert('Done', 'User added');
      setD({ u: '', e: '', p: '', f: '', l: '' });
    },
    onError: (er) => setErr(er.message),
  });

  const ch = (k, v) => setD({ ...d, [k]: v });

  return (
    <ScrollView style={s.c}>
      <Text style={s.t}>Add User</Text>
      
      <TextInput style={s.i} placeholder="Username *" value={d.u} onChangeText={v => ch('u', v)} />
      <TextInput style={s.i} placeholder="Email" value={d.e} keyboardType="email-address" onChangeText={v => ch('e', v)} />
      <TextInput style={s.i} placeholder="First" value={d.f} onChangeText={v => ch('f', v)} />
      <TextInput style={s.i} placeholder="Last" value={d.l} onChangeText={v => ch('l', v)} />
      <TextInput style={[s.i, s.p]} placeholder="Password" value={d.p} secureTextEntry onChangeText={v => ch('p', v)} />
      
      {err ? <Text style={s.err}>{err}</Text> : null}
      
      <TouchableOpacity style={s.b} onPress={() => mut.mutate({ username: d.u, email: d.e, password: d.p, first_name: d.f, last_name: d.l })} disabled={mut.isPending || !d.u}>
        <Text style={s.bt}>{mut.isPending ? 'Adding...' : 'Add'}</Text>
      </TouchableOpacity>
    </ScrollView>
  );
};

const s = StyleSheet.create({
  c: { flex: 1, padding: 20, backgroundColor: '#fff' },
  t: { fontSize: 24, fontWeight: 'bold', marginBottom: 20, textAlign: 'center' },
  i: { borderWidth: 1, borderColor: '#ddd', padding: 15, borderRadius: 8, marginBottom: 15, fontSize: 16 },
  p: { marginBottom: 20 },
  err: { color: 'red', marginBottom: 10 },
  b: { backgroundColor: '#007AFF', padding: 15, borderRadius: 8, alignItems: 'center' },
  bt: { color: '#fff', fontSize: 18, fontWeight: 'bold' },
});

export default AddUser;
