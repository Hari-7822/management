import React, { useState } from "react";
import { View, Text, TextInput, Switch, Button } from "react-native";

export default function FormBuilder({ schema, onSubmit }) {
  const [values, setValues] = useState({});

  const updateValue = (name, value) => {
    setValues(prev => ({ ...prev, [name]: value }));
  };

  const renderField = field => {
    switch (field.type) {
      case "text":
      case "password":
        return (
          <TextInput
            placeholder={field.placeholder}
            secureTextEntry={field.type === "password"}
            value={values[field.name] || ""}
            onChangeText={text => updateValue(field.name, text)}
            style={{ borderWidth: 1, padding: 10, marginVertical: 5 }}
          />
        );

      case "checkbox":
        return (
          <Switch
            value={!!values[field.name]}
            onValueChange={val => updateValue(field.name, val)}
          />
        );

      default:
        return null;
    }
  };

  return (
    <View>
      {schema.map(field => (
        <View key={field.name} style={{ marginBottom: 15 }}>
          <Text>{field.label}</Text>
          {renderField(field)}
        </View>
      ))}

      <Button title="Submit" onPress={() => onSubmit(values)} />
    </View>
  );
}
