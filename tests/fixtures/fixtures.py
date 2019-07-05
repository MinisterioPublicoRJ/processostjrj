wsdl = """

<?xml version="1.0" encoding="UTF-8"?>
<wsdl:definitions xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" xmlns:i0="http://tempuri.org/" xmlns:msc="http://schemas.microsoft.com/ws/2005/12/wsdl/contract" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:soap12="http://schemas.xmlsoap.org/wsdl/soap12/" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:tns="http://www.cnj.jus.br/servico-intercomunicacao-2.2.2/" xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:wsa10="http://www.w3.org/2005/08/addressing" xmlns:wsam="http://www.w3.org/2007/05/addressing/metadata" xmlns:wsap="http://schemas.xmlsoap.org/ws/2004/08/addressing/policy" xmlns:wsaw="http://www.w3.org/2006/05/addressing/wsdl" xmlns:wsp="http://schemas.xmlsoap.org/ws/2004/09/policy" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" xmlns:wsx="http://schemas.xmlsoap.org/ws/2004/09/mex" xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="Servico" targetNamespace="http://www.cnj.jus.br/servico-intercomunicacao-2.2.2/">
   <wsp:Policy wsu:Id="servico-intercomunicacao_policy">
      <wsp:ExactlyOne>
         <wsp:All>
            <sp:TransportBinding xmlns:sp="http://schemas.xmlsoap.org/ws/2005/07/securitypolicy">
               <wsp:Policy>
                  <sp:TransportToken>
                     <wsp:Policy>
                        <sp:HttpsToken RequireClientCertificate="false" />
                     </wsp:Policy>
                  </sp:TransportToken>
                  <sp:AlgorithmSuite>
                     <wsp:Policy>
                        <sp:Basic256 />
                     </wsp:Policy>
                  </sp:AlgorithmSuite>
                  <sp:Layout>
                     <wsp:Policy>
                        <sp:Strict />
                     </wsp:Policy>
                  </sp:Layout>
               </wsp:Policy>
            </sp:TransportBinding>
         </wsp:All>
      </wsp:ExactlyOne>
   </wsp:Policy>
   <wsdl:types>
      <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified" targetNamespace="http://www.cnj.jus.br/servico-intercomunicacao-2.2.2/">
         <xs:import namespace="http://www.cnj.jus.br/tipos-servico-intercomunicacao-2.2.2" />
         <xs:element xmlns:q1="http://www.cnj.jus.br/tipos-servico-intercomunicacao-2.2.2" name="consultarAvisosPendentes" type="q1:tipoConsultarAvisosPendentes" />
         <xs:element xmlns:q2="http://www.cnj.jus.br/tipos-servico-intercomunicacao-2.2.2" name="consultarAvisosPendentesResposta" type="q2:tipoConsultarAvisosPendentesResposta" />
         <xs:element xmlns:q3="http://www.cnj.jus.br/tipos-servico-intercomunicacao-2.2.2" name="consultarTeorComunicacao" type="q3:tipoConsultarTeorComunicacao" />
         <xs:element xmlns:q4="http://www.cnj.jus.br/tipos-servico-intercomunicacao-2.2.2" name="consultarTeorComunicacaoResposta" type="q4:tipoConsultarTeorComunicacaoResposta" />
         <xs:element xmlns:q5="http://www.cnj.jus.br/tipos-servico-intercomunicacao-2.2.2" name="consultarProcesso" type="q5:tipoConsultarProcesso" />
         <xs:element xmlns:q6="http://www.cnj.jus.br/tipos-servico-intercomunicacao-2.2.2" name="consultarProcessoResposta" type="q6:tipoConsultarProcessoResposta" />
         <xs:element xmlns:q7="http://www.cnj.jus.br/tipos-servico-intercomunicacao-2.2.2" name="entregarManifestacaoProcessual" type="q7:tipoEntregarManifestacaoProcessual" />
         <xs:element xmlns:q8="http://www.cnj.jus.br/tipos-servico-intercomunicacao-2.2.2" name="entregarManifestacaoProcessualResposta" type="q8:tipoEntregarManifestacaoProcessualResposta" />
         <xs:element xmlns:q9="http://www.cnj.jus.br/tipos-servico-intercomunicacao-2.2.2" name="consultarAlteracao" type="q9:tipoConsultarAlteracao" />
         <xs:element xmlns:q10="http://www.cnj.jus.br/tipos-servico-intercomunicacao-2.2.2" name="consultarAlteracaoResposta" type="q10:tipoConsultarAlteracaoResposta" />
         <xs:element xmlns:q11="http://www.cnj.jus.br/tipos-servico-intercomunicacao-2.2.2" name="confirmarRecebimento" type="q11:tipoConfirmarRecebimento" />
         <xs:element xmlns:q12="http://www.cnj.jus.br/tipos-servico-intercomunicacao-2.2.2" name="confirmarRecebimentoResposta" type="q12:tipoConfirmarRecebimentoResposta" />
      </xs:schema>
      <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:tns="http://www.cnj.jus.br/tipos-servico-intercomunicacao-2.2.2" elementFormDefault="qualified" targetNamespace="http://www.cnj.jus.br/tipos-servico-intercomunicacao-2.2.2">
         <xs:import namespace="http://www.cnj.jus.br/intercomunicacao-2.2.2" />
         <xs:complexType name="tipoConsultarAvisosPendentes">
            <xs:sequence>
               <xs:element minOccurs="0" maxOccurs="1" name="idRepresentado" type="xs:string" />
               <xs:element minOccurs="0" maxOccurs="1" name="idConsultante" type="xs:string" />
               <xs:element minOccurs="0" maxOccurs="1" name="senhaConsultante" type="xs:string" />
               <xs:element minOccurs="0" maxOccurs="1" name="dataReferencia" type="xs:string" />
               <xs:element minOccurs="0" maxOccurs="1" name="dataFimReferencia" type="xs:string" />
            </xs:sequence>
         </xs:complexType>
         <xs:complexType name="tipoConsultarAvisosPendentesResposta">
            <xs:sequence>
               <xs:element minOccurs="1" maxOccurs="1" name="sucesso" type="xs:boolean" />
               <xs:element minOccurs="0" maxOccurs="1" name="mensagem" type="xs:string" />
               <xs:element xmlns:q1="http://www.cnj.jus.br/intercomunicacao-2.2.2" minOccurs="0" maxOccurs="unbounded" name="aviso" type="q1:tipoAvisoComunicacaoPendente" />
            </xs:sequence>
         </xs:complexType>
         <xs:complexType name="tipoConsultarTeorComunicacao">
            <xs:sequence>
               <xs:element minOccurs="0" maxOccurs="1" name="idConsultante" type="xs:string" />
               <xs:element minOccurs="0" maxOccurs="1" name="senhaConsultante" type="xs:string" />
               <xs:choice minOccurs="1" maxOccurs="1">
                  <xs:element minOccurs="0" maxOccurs="1" name="numeroProcesso" type="xs:string" />
                  <xs:element minOccurs="0" maxOccurs="1" name="identificadorAviso" type="xs:string" />
               </xs:choice>
            </xs:sequence>
         </xs:complexType>
         <xs:complexType name="tipoConsultarTeorComunicacaoResposta">
            <xs:sequence>
               <xs:element minOccurs="1" maxOccurs="1" name="sucesso" type="xs:boolean" />
               <xs:element minOccurs="0" maxOccurs="1" name="mensagem" type="xs:string" />
               <xs:element xmlns:q2="http://www.cnj.jus.br/intercomunicacao-2.2.2" minOccurs="0" maxOccurs="unbounded" name="comunicacao" type="q2:tipoComunicacaoProcessual" />
            </xs:sequence>
         </xs:complexType>
         <xs:complexType name="tipoConsultarProcesso">
            <xs:sequence>
               <xs:element minOccurs="0" maxOccurs="1" name="idConsultante" type="xs:string" />
               <xs:element minOccurs="0" maxOccurs="1" name="senhaConsultante" type="xs:string" />
               <xs:element minOccurs="0" maxOccurs="1" name="numeroProcesso" type="xs:string" />
               <xs:element minOccurs="0" maxOccurs="1" name="dataReferencia" type="xs:string" />
               <xs:element minOccurs="0" maxOccurs="1" name="movimentos" type="xs:boolean" />
               <xs:choice minOccurs="0" maxOccurs="unbounded">
                  <xs:element minOccurs="0" maxOccurs="1" name="documento" type="xs:string" />
                  <xs:element minOccurs="1" maxOccurs="1" name="incluirDocumentos" type="xs:boolean" />
                  <xs:element minOccurs="1" maxOccurs="1" name="incluirCabecalho" type="xs:boolean" />
               </xs:choice>
            </xs:sequence>
         </xs:complexType>
         <xs:complexType name="tipoConsultarProcessoResposta">
            <xs:sequence>
               <xs:element minOccurs="1" maxOccurs="1" name="sucesso" type="xs:boolean" />
               <xs:element minOccurs="0" maxOccurs="1" name="mensagem" type="xs:string" />
               <xs:element xmlns:q3="http://www.cnj.jus.br/intercomunicacao-2.2.2" minOccurs="0" maxOccurs="1" name="processo" type="q3:tipoProcessoJudicial" />
            </xs:sequence>
         </xs:complexType>
         <xs:complexType name="tipoEntregarManifestacaoProcessual">
            <xs:sequence>
               <xs:element minOccurs="0" maxOccurs="1" name="idManifestante" type="xs:string" />
               <xs:element minOccurs="0" maxOccurs="1" name="senhaManifestante" type="xs:string" />
               <xs:choice minOccurs="1" maxOccurs="1">
                  <xs:element minOccurs="0" maxOccurs="1" name="numeroProcesso" type="xs:string" />
                  <xs:element xmlns:q4="http://www.cnj.jus.br/intercomunicacao-2.2.2" minOccurs="0" maxOccurs="1" name="dadosBasicos" type="q4:tipoCabecalhoProcesso" />
               </xs:choice>
               <xs:element xmlns:q5="http://www.cnj.jus.br/intercomunicacao-2.2.2" minOccurs="0" maxOccurs="unbounded" name="documento" type="q5:tipoDocumento" />
               <xs:element minOccurs="0" maxOccurs="1" name="dataEnvio" type="xs:string" />
               <xs:element xmlns:q6="http://www.cnj.jus.br/intercomunicacao-2.2.2" minOccurs="0" maxOccurs="unbounded" name="parametros" type="q6:tipoParametro" />
            </xs:sequence>
         </xs:complexType>
         <xs:complexType name="tipoEntregarManifestacaoProcessualResposta">
            <xs:sequence>
               <xs:element minOccurs="1" maxOccurs="1" name="sucesso" type="xs:boolean" />
               <xs:element minOccurs="0" maxOccurs="1" name="mensagem" type="xs:string" />
               <xs:element minOccurs="0" maxOccurs="1" name="protocoloRecebimento" type="xs:string" />
               <xs:element minOccurs="0" maxOccurs="1" name="dataOperacao" type="xs:string" />
               <xs:element minOccurs="0" maxOccurs="1" name="recibo" type="xs:base64Binary" />
               <xs:element xmlns:q7="http://www.cnj.jus.br/intercomunicacao-2.2.2" minOccurs="0" maxOccurs="unbounded" name="parametro" type="q7:tipoParametro" />
            </xs:sequence>
         </xs:complexType>
         <xs:complexType name="tipoConsultarAlteracao">
            <xs:sequence>
               <xs:element minOccurs="0" maxOccurs="1" name="idConsultante" type="xs:string" />
               <xs:element minOccurs="0" maxOccurs="1" name="senhaConsultante" type="xs:string" />
               <xs:element minOccurs="0" maxOccurs="1" name="numeroProcesso" type="xs:string" />
            </xs:sequence>
         </xs:complexType>
         <xs:complexType name="tipoConsultarAlteracaoResposta">
            <xs:sequence>
               <xs:element minOccurs="1" maxOccurs="1" name="sucesso" type="xs:boolean" />
               <xs:element minOccurs="0" maxOccurs="1" name="mensagem" type="xs:string" />
               <xs:element minOccurs="0" maxOccurs="1" name="hashCabecalho" type="xs:string" />
               <xs:element minOccurs="0" maxOccurs="1" name="hashMovimentacoes" type="xs:string" />
               <xs:element minOccurs="0" maxOccurs="1" name="hashDocumentos" type="xs:string" />
            </xs:sequence>
         </xs:complexType>
         <xs:complexType name="tipoConfirmarRecebimento">
            <xs:sequence>
               <xs:element minOccurs="0" maxOccurs="1" name="idRecebedor" type="xs:string" />
               <xs:element minOccurs="0" maxOccurs="1" name="senhaRecebedor" type="xs:string" />
               <xs:element minOccurs="0" maxOccurs="1" name="protocolo" type="xs:string" />
            </xs:sequence>
         </xs:complexType>
         <xs:complexType name="tipoConfirmarRecebimentoResposta">
            <xs:sequence>
               <xs:element minOccurs="1" maxOccurs="1" name="sucesso" type="xs:boolean" />
               <xs:element minOccurs="0" maxOccurs="1" name="mensagem" type="xs:string" />
            </xs:sequence>
         </xs:complexType>
      </xs:schema>
      <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:tns="http://www.cnj.jus.br/intercomunicacao-2.2.2" elementFormDefault="qualified" targetNamespace="http://www.cnj.jus.br/intercomunicacao-2.2.2">
         <xs:complexType name="tipoAvisoComunicacaoPendente">
            <xs:sequence>
               <xs:element minOccurs="0" maxOccurs="1" name="destinatario" type="tns:tipoParte" />
               <xs:element minOccurs="0" maxOccurs="1" name="processo" type="tns:tipoCabecalhoProcesso" />
               <xs:element minOccurs="0" maxOccurs="1" name="dataDisponibilizacao" type="xs:string" />
            </xs:sequence>
            <xs:attribute name="tipoComunicacao" type="xs:string" />
            <xs:attribute name="idAviso" type="xs:string" />
         </xs:complexType>
         <xs:complexType name="tipoParte">
            <xs:sequence>
               <xs:choice minOccurs="1" maxOccurs="1">
                  <xs:element minOccurs="0" maxOccurs="1" name="pessoa" type="tns:tipoPessoa" />
                  <xs:element minOccurs="0" maxOccurs="1" name="interessePublico" type="xs:string" />
               </xs:choice>
               <xs:element minOccurs="0" maxOccurs="unbounded" name="advogado" type="tns:tipoRepresentanteProcessual" />
               <xs:element minOccurs="0" maxOccurs="unbounded" name="pessoaProcessualRelacionada" type="tns:tipoParte" />
            </xs:sequence>
            <xs:attribute name="relacionamentoProcessual" type="tns:modalidadeRelacionamentoProcessual" />
            <xs:attribute name="intimacaoPendente" type="xs:int" />
            <xs:attribute name="assistenciaJudiciaria" type="xs:boolean" />
         </xs:complexType>
         <xs:complexType name="tipoPessoa">
            <xs:sequence>
               <xs:element minOccurs="0" maxOccurs="unbounded" name="outroNome" type="xs:string" />
               <xs:element minOccurs="0" maxOccurs="unbounded" name="documento" type="tns:tipoDocumentoIdentificacao" />
               <xs:element minOccurs="0" maxOccurs="unbounded" name="endereco" type="tns:tipoEndereco" />
               <xs:element minOccurs="0" maxOccurs="unbounded" name="pessoaRelacionada" nillable="true" type="tns:tipoRelacionamentoPessoal" />
               <xs:element minOccurs="0" maxOccurs="1" name="pessoaVinculada" type="tns:tipoPessoa" />
            </xs:sequence>
            <xs:attribute name="tipoPessoa" type="tns:tipoQualificacaoPessoa" use="required" />
            <xs:attribute name="numeroDocumentoPrincipal" type="xs:string" />
            <xs:attribute name="cidadeNatural" type="xs:string" />
            <xs:attribute default="BR" name="nacionalidade" type="xs:string" />
            <xs:attribute name="estadoNatural" type="xs:string" />
            <xs:attribute name="dataObito" type="xs:string" />
            <xs:attribute name="sexo" type="tns:modalidadeGeneroPessoa" use="required" />
            <xs:attribute name="nome" type="xs:string" />
            <xs:attribute name="nomeGenitor" type="xs:string" />
            <xs:attribute name="dataNascimento" type="xs:string" />
            <xs:attribute name="nomeGenitora" type="xs:string" />
         </xs:complexType>
         <xs:complexType name="tipoDocumentoIdentificacao">
            <xs:attribute name="codigoDocumento" type="xs:string" />
            <xs:attribute name="emissorDocumento" type="xs:string" />
            <xs:attribute name="tipoDocumento" type="tns:modalidadeDocumentoIdentificador" use="required" />
            <xs:attribute name="nome" type="xs:string" />
         </xs:complexType>
         <xs:simpleType name="modalidadeDocumentoIdentificador">
            <xs:restriction base="xs:string">
               <xs:enumeration value="CI" />
               <xs:enumeration value="CNH" />
               <xs:enumeration value="TE" />
               <xs:enumeration value="CN" />
               <xs:enumeration value="CC" />
               <xs:enumeration value="PAS" />
               <xs:enumeration value="CT" />
               <xs:enumeration value="RIC" />
               <xs:enumeration value="CMF" />
               <xs:enumeration value="PIS_PASEP" />
               <xs:enumeration value="CEI" />
               <xs:enumeration value="NIT" />
               <xs:enumeration value="CP" />
               <xs:enumeration value="IF" />
               <xs:enumeration value="OAB" />
               <xs:enumeration value="RJC" />
               <xs:enumeration value="RGE" />
            </xs:restriction>
         </xs:simpleType>
         <xs:complexType name="tipoEndereco">
            <xs:sequence>
               <xs:element minOccurs="0" maxOccurs="1" name="logradouro" type="xs:string" />
               <xs:element minOccurs="0" maxOccurs="1" name="numero" type="xs:string" />
               <xs:element minOccurs="0" maxOccurs="1" name="complemento" type="xs:string" />
               <xs:element minOccurs="0" maxOccurs="1" name="bairro" type="xs:string" />
               <xs:element minOccurs="0" maxOccurs="1" name="cidade" type="xs:string" />
               <xs:element minOccurs="0" maxOccurs="1" name="estado" type="xs:string" />
               <xs:element minOccurs="0" maxOccurs="1" name="pais" type="xs:string" />
            </xs:sequence>
            <xs:attribute name="cep" type="xs:string" />
         </xs:complexType>
         <xs:complexType name="tipoRelacionamentoPessoal">
            <xs:sequence>
               <xs:element minOccurs="0" maxOccurs="1" name="pessoa" type="tns:tipoPessoa" />
            </xs:sequence>
            <xs:attribute name="modalidadeRelacionamento" type="tns:modalidadesRelacionamentoPessoal" />
         </xs:complexType>
         <xs:simpleType name="modalidadesRelacionamentoPessoal">
            <xs:restriction base="xs:string">
               <xs:enumeration value="P" />
               <xs:enumeration value="AP" />
               <xs:enumeration value="SP" />
               <xs:enumeration value="T" />
               <xs:enumeration value="C" />
            </xs:restriction>
         </xs:simpleType>
         <xs:simpleType name="tipoQualificacaoPessoa">
            <xs:restriction base="xs:string">
               <xs:enumeration value="fisica" />
               <xs:enumeration value="juridica" />
               <xs:enumeration value="autoridade" />
               <xs:enumeration value="orgaorepresentacao" />
            </xs:restriction>
         </xs:simpleType>
         <xs:simpleType name="modalidadeGeneroPessoa">
            <xs:restriction base="xs:string">
               <xs:enumeration value="M" />
               <xs:enumeration value="F" />
               <xs:enumeration value="D" />
            </xs:restriction>
         </xs:simpleType>
         <xs:complexType name="tipoRepresentanteProcessual">
            <xs:sequence>
               <xs:element minOccurs="0" maxOccurs="unbounded" name="endereco" type="tns:tipoEndereco" />
            </xs:sequence>
            <xs:attribute name="intimacao" type="xs:boolean" use="required" />
            <xs:attribute name="tipoRepresentante" type="tns:modalidadeRepresentanteProcessual" use="required" />
            <xs:attribute name="numeroDocumentoPrincipal" type="xs:string" />
            <xs:attribute name="nome" type="xs:string" />
            <xs:attribute name="inscricao" type="xs:string" />
         </xs:complexType>
         <xs:simpleType name="modalidadeRepresentanteProcessual">
            <xs:restriction base="xs:string">
               <xs:enumeration value="A" />
               <xs:enumeration value="E" />
               <xs:enumeration value="M" />
               <xs:enumeration value="D" />
               <xs:enumeration value="P" />
            </xs:restriction>
         </xs:simpleType>
         <xs:simpleType name="modalidadeRelacionamentoProcessual">
            <xs:restriction base="xs:string">
               <xs:enumeration value="CP" />
               <xs:enumeration value="RP" />
               <xs:enumeration value="TF" />
               <xs:enumeration value="AT" />
               <xs:enumeration value="AS" />
            </xs:restriction>
         </xs:simpleType>
         <xs:complexType name="tipoCabecalhoProcesso">
            <xs:sequence>
               <xs:element minOccurs="0" maxOccurs="unbounded" name="polo" type="tns:tipoPoloProcessual" />
               <xs:element minOccurs="0" maxOccurs="unbounded" name="assunto" type="tns:tipoAssuntoProcessual" />
               <xs:element minOccurs="0" maxOccurs="unbounded" name="magistradoAtuante" type="xs:string" />
               <xs:element minOccurs="0" maxOccurs="unbounded" name="processoVinculado" type="tns:tipoVinculacaoProcessual" />
               <xs:element minOccurs="0" maxOccurs="unbounded" name="prioridade" type="xs:string" />
               <xs:element minOccurs="0" maxOccurs="unbounded" name="outroParametro" type="tns:tipoParametro" />
               <xs:element minOccurs="0" maxOccurs="1" name="valorCausa" type="xs:double" />
               <xs:element minOccurs="0" maxOccurs="1" name="orgaoJulgador" type="tns:tipoOrgaoJulgador" />
               <xs:element minOccurs="0" maxOccurs="unbounded" name="outrosnumeros" type="xs:string" />
            </xs:sequence>
            <xs:attribute name="intervencaoMP" type="xs:boolean" />
            <xs:attribute name="nivelSigilo" type="xs:int" use="required" />
            <xs:attribute name="dataAjuizamento" type="xs:string" />
            <xs:attribute name="tamanhoProcesso" type="xs:int" />
            <xs:attribute name="competencia" type="xs:int" />
            <xs:attribute name="numero" type="xs:string" />
            <xs:attribute name="codigoLocalidade" type="xs:string" />
            <xs:attribute name="classeProcessual" type="xs:int" use="required" />
         </xs:complexType>
         <xs:complexType name="tipoPoloProcessual">
            <xs:sequence>
               <xs:element minOccurs="0" maxOccurs="unbounded" name="parte" type="tns:tipoParte" />
            </xs:sequence>
            <xs:attribute name="polo" type="tns:modalidadePoloProcessual" />
         </xs:complexType>
         <xs:simpleType name="modalidadePoloProcessual">
            <xs:restriction base="xs:string">
               <xs:enumeration value="AT" />
               <xs:enumeration value="PA" />
               <xs:enumeration value="TC" />
               <xs:enumeration value="FL" />
               <xs:enumeration value="TJ" />
               <xs:enumeration value="AD" />
               <xs:enumeration value="VI" />
            </xs:restriction>
         </xs:simpleType>
         <xs:complexType name="tipoAssuntoProcessual">
            <xs:sequence>
               <xs:choice minOccurs="1" maxOccurs="1">
                  <xs:element minOccurs="1" maxOccurs="1" name="codigoNacional" type="xs:int" />
                  <xs:element minOccurs="0" maxOccurs="1" name="assuntoLocal" type="tns:tipoAssuntoLocal" />
               </xs:choice>
            </xs:sequence>
            <xs:attribute default="false" name="principal" type="xs:boolean" />
         </xs:complexType>
         <xs:complexType name="tipoAssuntoLocal">
            <xs:sequence>
               <xs:element minOccurs="0" maxOccurs="1" name="assuntoLocalPai" type="tns:tipoAssuntoLocal" />
            </xs:sequence>
            <xs:attribute name="descricao" type="xs:string" />
            <xs:attribute name="codigoPaiNacional" type="xs:int" use="required" />
            <xs:attribute name="codigoAssunto" type="xs:int" use="required" />
         </xs:complexType>
         <xs:complexType name="tipoVinculacaoProcessual">
            <xs:attribute name="numeroProcesso" type="xs:string" />
            <xs:attribute name="vinculo" type="tns:modalidadeVinculacaoProcesso" use="required" />
         </xs:complexType>
         <xs:simpleType name="modalidadeVinculacaoProcesso">
            <xs:restriction base="xs:string">
               <xs:enumeration value="CX" />
               <xs:enumeration value="CT" />
               <xs:enumeration value="DP" />
               <xs:enumeration value="AR" />
               <xs:enumeration value="CD" />
               <xs:enumeration value="OR" />
               <xs:enumeration value="RR" />
               <xs:enumeration value="RG" />
            </xs:restriction>
         </xs:simpleType>
         <xs:complexType name="tipoParametro">
            <xs:attribute name="nome" type="xs:string" />
            <xs:attribute name="valor" type="xs:string" />
         </xs:complexType>
         <xs:complexType name="tipoOrgaoJulgador">
            <xs:attribute name="codigoOrgao" type="xs:string" />
            <xs:attribute name="nomeOrgao" type="xs:string" />
            <xs:attribute name="instancia" use="required">
               <xs:simpleType>
                  <xs:restriction base="xs:string">
                     <xs:enumeration value="ORIG" />
                     <xs:enumeration value="REV" />
                     <xs:enumeration value="ESP" />
                     <xs:enumeration value="EXT" />
                     <xs:enumeration value="ADM" />
                  </xs:restriction>
               </xs:simpleType>
            </xs:attribute>
            <xs:attribute name="codigoMunicipioIBGE" type="xs:int" use="required" />
         </xs:complexType>
         <xs:complexType name="tipoComunicacaoProcessual">
            <xs:sequence>
               <xs:element minOccurs="0" maxOccurs="1" name="destinatario" type="tns:tipoParte" />
               <xs:element minOccurs="0" maxOccurs="1" name="processo" type="xs:string" />
               <xs:element minOccurs="0" maxOccurs="1" name="teor" type="xs:string" />
               <xs:element minOccurs="0" maxOccurs="unbounded" name="documento" type="tns:tipoDocumento" />
               <xs:element minOccurs="0" maxOccurs="unbounded" name="parametro" type="xs:string" />
               <xs:any minOccurs="0" maxOccurs="1" />
            </xs:sequence>
            <xs:attribute name="dataReferencia" type="xs:string" />
            <xs:attribute name="prazo" type="xs:int" />
            <xs:attribute name="nivelSigilo" type="xs:int" />
            <xs:attribute name="id" type="xs:string" />
            <xs:attribute name="tipoComunicacao" type="xs:string" />
            <xs:attribute name="tipoPrazo" type="tns:tipoPrazo" />
         </xs:complexType>
         <xs:complexType name="tipoDocumento">
            <xs:sequence>
               <xs:element minOccurs="0" maxOccurs="1" name="conteudo" type="xs:base64Binary" />
               <xs:element minOccurs="0" maxOccurs="unbounded" name="assinatura" type="tns:tipoAssinatura" />
               <xs:element minOccurs="0" maxOccurs="unbounded" name="outroParametro" type="tns:tipoParametro" />
               <xs:any minOccurs="0" maxOccurs="1" />
               <xs:element minOccurs="0" maxOccurs="unbounded" name="documentoVinculado" type="tns:tipoDocumento" />
            </xs:sequence>
            <xs:attribute name="movimento" type="xs:int" />
            <xs:attribute name="nivelSigilo" type="xs:int" />
            <xs:attribute name="hash" type="xs:string" />
            <xs:attribute name="tipoDocumentoLocal" type="xs:string" />
            <xs:attribute name="descricao" type="xs:string" />
            <xs:attribute name="idDocumentoVinculado" type="xs:string" />
            <xs:attribute name="idDocumento" type="xs:string" />
            <xs:attribute name="tipoDocumento" type="xs:string" />
            <xs:attribute name="mimetype" type="xs:string" />
            <xs:attribute name="dataHora" type="xs:string" />
         </xs:complexType>
         <xs:complexType name="tipoAssinatura">
            <xs:sequence>
               <xs:element minOccurs="0" maxOccurs="unbounded" name="signatarioLogin" type="tns:tipoSignatarioSimples" />
            </xs:sequence>
            <xs:attribute name="algoritmoHash" type="xs:string" />
            <xs:attribute name="codificacaoCertificado" type="xs:string" />
            <xs:attribute name="cadeiaCertificado" type="xs:string" />
            <xs:attribute name="assinatura" type="xs:string" />
            <xs:attribute name="dataAssinatura" type="xs:string" />
         </xs:complexType>
         <xs:complexType name="tipoSignatarioSimples">
            <xs:attribute name="identificador" type="xs:string" />
            <xs:attribute name="dataHora" type="xs:string" />
         </xs:complexType>
         <xs:simpleType name="tipoPrazo">
            <xs:restriction base="xs:string">
               <xs:enumeration value="HOR" />
               <xs:enumeration value="DIA" />
               <xs:enumeration value="MES" />
               <xs:enumeration value="ANO" />
               <xs:enumeration value="DATA_CERTA" />
               <xs:enumeration value="SEMPRAZO" />
            </xs:restriction>
         </xs:simpleType>
         <xs:complexType name="tipoProcessoJudicial">
            <xs:sequence>
               <xs:element minOccurs="0" maxOccurs="1" name="dadosBasicos" type="tns:tipoCabecalhoProcesso" />
               <xs:element minOccurs="0" maxOccurs="unbounded" name="movimento" type="tns:tipoMovimentoProcessual" />
               <xs:element minOccurs="0" maxOccurs="unbounded" name="documento" type="tns:tipoDocumento" />
            </xs:sequence>
         </xs:complexType>
         <xs:complexType name="tipoMovimentoProcessual">
            <xs:sequence>
               <xs:element minOccurs="0" maxOccurs="unbounded" name="complemento" type="xs:string" />
               <xs:choice minOccurs="1" maxOccurs="1">
                  <xs:element minOccurs="0" maxOccurs="1" name="movimentoLocal" type="tns:tipoMovimentoLocal" />
                  <xs:element minOccurs="0" maxOccurs="1" name="movimentoNacional" type="tns:tipoMovimentoNacional" />
               </xs:choice>
               <xs:element minOccurs="0" maxOccurs="unbounded" name="idDocumentoVinculado" type="xs:string" />
            </xs:sequence>
            <xs:attribute name="identificadorMovimento" type="xs:string" />
            <xs:attribute name="nivelSigilo" type="xs:int" />
            <xs:attribute name="dataHora" type="xs:string" />
         </xs:complexType>
         <xs:complexType name="tipoMovimentoLocal">
            <xs:sequence>
               <xs:element minOccurs="0" maxOccurs="1" name="movimentoLocalPai" type="tns:tipoMovimentoLocal" />
            </xs:sequence>
            <xs:attribute name="descricao" type="xs:string" />
            <xs:attribute name="codigoPaiNacional" type="xs:int" use="required" />
            <xs:attribute name="codigoMovimento" type="xs:int" use="required" />
         </xs:complexType>
         <xs:complexType name="tipoMovimentoNacional">
            <xs:sequence>
               <xs:element minOccurs="0" maxOccurs="unbounded" name="complemento" type="xs:string" />
            </xs:sequence>
            <xs:attribute name="codigoNacional" type="xs:int" use="required" />
         </xs:complexType>
      </xs:schema>
   </wsdl:types>
   <wsdl:message name="consultarAvisosPendentesRequest">
      <wsdl:part name="consultarAvisosPendentes" element="tns:consultarAvisosPendentes" />
   </wsdl:message>
   <wsdl:message name="consultarAvisosPendentesResponse">
      <wsdl:part name="consultarAvisosPendentesResposta" element="tns:consultarAvisosPendentesResposta" />
   </wsdl:message>
   <wsdl:message name="consultarTeorComunicacaoRequest">
      <wsdl:part name="consultarTeorComunicacao" element="tns:consultarTeorComunicacao" />
   </wsdl:message>
   <wsdl:message name="consultarTeorComunicacaoResponse">
      <wsdl:part name="consultarTeorComunicacaoResposta" element="tns:consultarTeorComunicacaoResposta" />
   </wsdl:message>
   <wsdl:message name="consultarProcessoRequest">
      <wsdl:part name="consultarProcesso" element="tns:consultarProcesso" />
   </wsdl:message>
   <wsdl:message name="consultarProcessoResponse">
      <wsdl:part name="consultarProcessoResposta" element="tns:consultarProcessoResposta" />
   </wsdl:message>
   <wsdl:message name="entregarManifestacaoProcessualRequest">
      <wsdl:part name="entregarManifestacaoProcessual" element="tns:entregarManifestacaoProcessual" />
   </wsdl:message>
   <wsdl:message name="entregarManifestacaoProcessualResponse">
      <wsdl:part name="entregarManifestacaoProcessualResposta" element="tns:entregarManifestacaoProcessualResposta" />
   </wsdl:message>
   <wsdl:message name="consultarAlteracaoRequest">
      <wsdl:part name="consultarAlteracao" element="tns:consultarAlteracao" />
   </wsdl:message>
   <wsdl:message name="consultarAlteracaoResponse">
      <wsdl:part name="consultarAlteracaoResposta" element="tns:consultarAlteracaoResposta" />
   </wsdl:message>
   <wsdl:message name="confirmarRecebimentoRequest">
      <wsdl:part name="confirmarRecebimento" element="tns:confirmarRecebimento" />
   </wsdl:message>
   <wsdl:message name="confirmarRecebimentoResponse">
      <wsdl:part name="confirmarRecebimentoResposta" element="tns:confirmarRecebimentoResposta" />
   </wsdl:message>
   <wsdl:portType name="servico-intercomunicacao-2.2.2">
      <wsdl:operation name="consultarAvisosPendentes">
         <wsdl:input wsaw:Action="http://www.cnj.jus.br/servico-intercomunicacao-2.2.2/consultarAvisosPendentes" name="consultarAvisosPendentesRequest" message="tns:consultarAvisosPendentesRequest" />
         <wsdl:output wsaw:Action="http://www.cnj.jus.br/servico-intercomunicacao-2.2.2/servico-intercomunicacao-2.2.2/consultarAvisosPendentesResponse" name="consultarAvisosPendentesResponse" message="tns:consultarAvisosPendentesResponse" />
      </wsdl:operation>
      <wsdl:operation name="consultarTeorComunicacao">
         <wsdl:input wsaw:Action="http://www.cnj.jus.br/servico-intercomunicacao-2.2.2/consultarTeorComunicacao" name="consultarTeorComunicacaoRequest" message="tns:consultarTeorComunicacaoRequest" />
         <wsdl:output wsaw:Action="http://www.cnj.jus.br/servico-intercomunicacao-2.2.2/servico-intercomunicacao-2.2.2/consultarTeorComunicacaoResponse" name="consultarTeorComunicacaoResponse" message="tns:consultarTeorComunicacaoResponse" />
      </wsdl:operation>
      <wsdl:operation name="consultarProcesso">
         <wsdl:input wsaw:Action="http://www.cnj.jus.br/servico-intercomunicacao-2.2.2/consultarProcesso" name="consultarProcessoRequest" message="tns:consultarProcessoRequest" />
         <wsdl:output wsaw:Action="http://www.cnj.jus.br/servico-intercomunicacao-2.2.2/servico-intercomunicacao-2.2.2/consultarProcessoResponse" name="consultarProcessoResponse" message="tns:consultarProcessoResponse" />
      </wsdl:operation>
      <wsdl:operation name="entregarManifestacaoProcessual">
         <wsdl:input wsaw:Action="http://www.cnj.jus.br/servico-intercomunicacao-2.2.2/entregarManifestacaoProcessual" name="entregarManifestacaoProcessualRequest" message="tns:entregarManifestacaoProcessualRequest" />
         <wsdl:output wsaw:Action="http://www.cnj.jus.br/servico-intercomunicacao-2.2.2/servico-intercomunicacao-2.2.2/entregarManifestacaoProcessualResponse" name="entregarManifestacaoProcessualResponse" message="tns:entregarManifestacaoProcessualResponse" />
      </wsdl:operation>
      <wsdl:operation name="consultarAlteracao">
         <wsdl:input wsaw:Action="http://www.cnj.jus.br/servico-intercomunicacao-2.2.2/consultarAlteracao" name="consultarAlteracaoRequest" message="tns:consultarAlteracaoRequest" />
         <wsdl:output wsaw:Action="http://www.cnj.jus.br/servico-intercomunicacao-2.2.2/servico-intercomunicacao-2.2.2/consultarAlteracaoResponse" name="consultarAlteracaoResponse" message="tns:consultarAlteracaoResponse" />
      </wsdl:operation>
      <wsdl:operation name="confirmarRecebimento">
         <wsdl:input wsaw:Action="http://www.cnj.jus.br/servico-intercomunicacao-2.2.2/confirmarRecebimento" name="confirmarRecebimentoRequest" message="tns:confirmarRecebimentoRequest" />
         <wsdl:output wsaw:Action="http://www.cnj.jus.br/servico-intercomunicacao-2.2.2/servico-intercomunicacao-2.2.2/confirmarRecebimentoResponse" name="confirmarRecebimentoResponse" message="tns:confirmarRecebimentoResponse" />
      </wsdl:operation>
   </wsdl:portType>
   <wsdl:binding name="servico-intercomunicacao" type="tns:servico-intercomunicacao-2.2.2">
      <wsp:PolicyReference URI="#servico-intercomunicacao_policy" />
      <soap:binding transport="http://schemas.xmlsoap.org/soap/http" />
      <wsdl:operation name="consultarAvisosPendentes">
         <soap:operation soapAction="http://www.cnj.jus.br/servico-intercomunicacao-2.2.2/consultarAvisosPendentes" style="document" />
         <wsdl:input name="consultarAvisosPendentesRequest">
            <soap:body use="literal" />
         </wsdl:input>
         <wsdl:output name="consultarAvisosPendentesResponse">
            <soap:body use="literal" />
         </wsdl:output>
      </wsdl:operation>
      <wsdl:operation name="consultarTeorComunicacao">
         <soap:operation soapAction="http://www.cnj.jus.br/servico-intercomunicacao-2.2.2/consultarTeorComunicacao" style="document" />
         <wsdl:input name="consultarTeorComunicacaoRequest">
            <soap:body use="literal" />
         </wsdl:input>
         <wsdl:output name="consultarTeorComunicacaoResponse">
            <soap:body use="literal" />
         </wsdl:output>
      </wsdl:operation>
      <wsdl:operation name="consultarProcesso">
         <soap:operation soapAction="http://www.cnj.jus.br/servico-intercomunicacao-2.2.2/consultarProcesso" style="document" />
         <wsdl:input name="consultarProcessoRequest">
            <soap:body use="literal" />
         </wsdl:input>
         <wsdl:output name="consultarProcessoResponse">
            <soap:body use="literal" />
         </wsdl:output>
      </wsdl:operation>
      <wsdl:operation name="entregarManifestacaoProcessual">
         <soap:operation soapAction="http://www.cnj.jus.br/servico-intercomunicacao-2.2.2/entregarManifestacaoProcessual" style="document" />
         <wsdl:input name="entregarManifestacaoProcessualRequest">
            <soap:body use="literal" />
         </wsdl:input>
         <wsdl:output name="entregarManifestacaoProcessualResponse">
            <soap:body use="literal" />
         </wsdl:output>
      </wsdl:operation>
      <wsdl:operation name="consultarAlteracao">
         <soap:operation soapAction="http://www.cnj.jus.br/servico-intercomunicacao-2.2.2/consultarAlteracao" style="document" />
         <wsdl:input name="consultarAlteracaoRequest">
            <soap:body use="literal" />
         </wsdl:input>
         <wsdl:output name="consultarAlteracaoResponse">
            <soap:body use="literal" />
         </wsdl:output>
      </wsdl:operation>
      <wsdl:operation name="confirmarRecebimento">
         <soap:operation soapAction="http://www.cnj.jus.br/servico-intercomunicacao-2.2.2/confirmarRecebimento" style="document" />
         <wsdl:input name="confirmarRecebimentoRequest">
            <soap:body use="literal" />
         </wsdl:input>
         <wsdl:output name="confirmarRecebimentoResponse">
            <soap:body use="literal" />
         </wsdl:output>
      </wsdl:operation>
   </wsdl:binding>
   <wsdl:service name="Servico">
      <wsdl:port name="servico-intercomunicacao" binding="tns:servico-intercomunicacao">
         <soap:address location="https://webserverseguro.tjrj.jus.br/MNI/Servico.svc" />
      </wsdl:port>
   </wsdl:service>
</wsdl:definitions>"""
