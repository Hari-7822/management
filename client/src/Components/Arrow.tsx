import React, { useState, useMemo } from 'react';
import { View, ScrollView } from 'react-native';
import { DataTable, IconButton, Text, MD3LightTheme as DefaultTheme, Provider as PaperProvider, Colors } from 'react-native-paper';
import MaterialCommunityIcons from '@expo/vector-icons/MaterialCommunityIcons';
import { useQuery } from '@tanstack/react-query';
import axios from 'axios';

type SortDir = 'asc' | 'desc' | null;
type Sort = { field: string | null; dir: SortDir };
type Row = { id: number; name: string; age: number };
type Props = { url: string };

async function getRows(url: string, s: Sort) {
  const params: Record<string, string> = {};
  if (s.field && s.dir) {
    params.by = s.field;
    params.dir = s.dir;
  }
  const res = await axios.get<Row[]>(url, { params });
  return res.data;
}

const theme = {
  ...DefaultTheme,
  colors: {
    ...DefaultTheme.colors,
    primary: 'rgb(0, 122, 255)' as Colors,
  },
};

export function SortTable({ url }: Props) {
  const [sort, setSort] = useState<Sort>({ field: null, dir: null });

  const qKey = useMemo(
    () => ['rows', { field: sort.field, dir: sort.dir }],
    [sort.field, sort.dir]
  );

  const { data, isLoading, isError } = useQuery({
    queryKey: qKey,
    queryFn: () => getRows(url, sort),
    keepPreviousData: true,
  });

  const onSort = (field: string) => {
    setSort(cur => {
      if (cur.field !== field) return { field, dir: 'asc' };
      if (cur.dir === 'asc') return { field, dir: 'desc' };
      return { field: null, dir: null };
    });
  };

  const sortIcon = (field: string) => {
    if (sort.field !== field || !sort.dir) return 'unfold-more-horizontal';
    return sort.dir === 'asc' ? 'arrow-up' : 'arrow-down';
  };

  return (
    <PaperProvider theme={theme}>
      <ScrollView horizontal style={{ padding: 16 }}>
        <DataTable>
          <DataTable.Header>
            <DataTable.Title>
              <Text>Name</Text>
              <IconButton icon={sortIcon('name')} size={20} onPress={() => onSort('name')} />
            </DataTable.Title>
            <DataTable.Title>
              <Text>Age</Text>
              <IconButton icon={sortIcon('age')} size={20} onPress={() => onSort('age')} />
            </DataTable.Title>
          </DataTable.Header>
          {isLoading && (
            <DataTable.Row>
              <DataTable.Cell><Text>Loading...</Text></DataTable.Cell>
              <DataTable.Cell />
            </DataTable.Row>
          )}
          {isError && !isLoading && (
            <DataTable.Row>
              <DataTable.Cell colSpan={2}><Text style={{ color: 'red' }}>Failed to load</Text></DataTable.Cell>
            </DataTable.Row>
          )}
          {!isLoading &&
            !isError &&
            data?.map(r => (
              <DataTable.Row key={r.id}>
                <DataTable.Cell><Text>{r.name}</Text></DataTable.Cell>
                <DataTable.Cell><Text>{r.age}</Text></DataTable.Cell>
              </DataTable.Row>
            ))}
        </DataTable>
      </ScrollView>
    </PaperProvider>
  );
}
